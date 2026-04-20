from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas, services
from .database import Base, engine, get_db

app = FastAPI(title="Restaurante Digital API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)
    db = next(get_db())
    try:
        services.seed_dishes(db)
    finally:
        db.close()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/dishes", response_model=list[schemas.DishOut])
def list_dishes(db: Session = Depends(get_db)):
    return db.query(models.Dish).filter(models.Dish.is_active.is_(True)).all()


@app.post("/orders", response_model=schemas.OrderOut, status_code=201)
def create_order(payload: schemas.OrderCreate, db: Session = Depends(get_db)):
    order = services.create_order(db, payload)
    order = services.get_order(db, order.id)
    return services.format_order(order)


@app.get("/orders/{order_id}", response_model=schemas.OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = services.get_order(db, order_id)
    return services.format_order(order)


@app.post("/orders/{order_id}/payments", response_model=schemas.PaymentOut, status_code=201)
def pay_order(order_id: int, payload: schemas.PaymentCreate, db: Session = Depends(get_db)):
    payment = services.process_payment(db, order_id, payload)
    return payment


# Servir archivos estáticos (HTML, CSS, JS) al final
from pathlib import Path
from fastapi.staticfiles import StaticFiles
static_dir = str(Path(__file__).parent.parent)
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
