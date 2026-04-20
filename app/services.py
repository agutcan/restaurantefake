from decimal import Decimal

from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from . import models
from .schemas import OrderCreate, OrderOut, OrderItemOut, PaymentCreate


def _to_decimal(value: float | str | Decimal) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"))


def seed_dishes(db: Session) -> None:
    if db.query(models.Dish).count() > 0:
        return

    dishes = [
        models.Dish(
            name="Hamburguesa Codigo",
            category="Gourmet",
            description="Carne 180g, cheddar, salsa de la casa",
            price=_to_decimal("12.50"),
        ),
        models.Dish(
            name="Pizza Deploy",
            category="Pizza",
            description="Masa artesanal, mozzarella, albahaca",
            price=_to_decimal("11.00"),
        ),
        models.Dish(
            name="Limonada Stack",
            category="Bebida",
            description="Limon natural, hierbabuena, hielo",
            price=_to_decimal("4.20"),
        ),
        models.Dish(
            name="Brownie Merge",
            category="Postre",
            description="Chocolate 70%, nueces, helado vainilla",
            price=_to_decimal("5.80"),
        ),
    ]
    db.add_all(dishes)
    db.commit()


def create_order(db: Session, payload: OrderCreate) -> models.Order:
    if not payload.items:
        raise HTTPException(status_code=400, detail="El pedido debe incluir al menos un plato")

    order = models.Order(status="pending", subtotal=_to_decimal(0), total=_to_decimal(0))
    db.add(order)
    db.flush()

    subtotal = Decimal("0.00")

    for item in payload.items:
        dish = db.get(models.Dish, item.dish_id)
        if not dish or not dish.is_active:
            raise HTTPException(status_code=404, detail=f"Plato no disponible: {item.dish_id}")

        unit_price = _to_decimal(dish.price)
        line_total = unit_price * item.quantity
        subtotal += line_total

        db_item = models.OrderItem(
            order_id=order.id,
            dish_id=dish.id,
            quantity=item.quantity,
            unit_price=unit_price,
            line_total=line_total,
        )
        db.add(db_item)

    order.subtotal = subtotal
    order.total = subtotal
    db.commit()
    db.refresh(order)
    return order


def get_order(db: Session, order_id: int) -> models.Order:
    order = (
        db.query(models.Order)
        .options(joinedload(models.Order.items).joinedload(models.OrderItem.dish))
        .filter(models.Order.id == order_id)
        .first()
    )
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return order


def format_order(order: models.Order) -> OrderOut:
    items = [
        OrderItemOut(
            dish_id=item.dish_id,
            dish_name=item.dish.name,
            quantity=item.quantity,
            unit_price=float(item.unit_price),
            line_total=float(item.line_total),
        )
        for item in order.items
    ]

    return OrderOut(
        id=order.id,
        status=order.status,
        subtotal=float(order.subtotal),
        total=float(order.total),
        created_at=order.created_at,
        items=items,
    )


def process_payment(db: Session, order_id: int, payload: PaymentCreate) -> models.Payment:
    order = get_order(db, order_id)

    if order.status == "paid":
        raise HTTPException(status_code=400, detail="El pedido ya fue pagado")

    total = _to_decimal(order.total)
    amount_paid = _to_decimal(payload.amount_paid)

    if amount_paid < total:
        raise HTTPException(status_code=400, detail="Fondos insuficientes")

    change_amount = amount_paid - total if payload.method == "cash" else Decimal("0.00")

    payment = models.Payment(
        order_id=order.id,
        method=payload.method,
        amount_paid=amount_paid,
        change_amount=change_amount,
        status="approved",
    )

    order.status = "paid"
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment
