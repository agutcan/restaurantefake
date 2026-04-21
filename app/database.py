"""Configuracion de base de datos y helpers de ciclo de vida de sesiones SQLAlchemy."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://app_user:app_pass@db:5432/restaurante",
)

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Entrega una sesion de BD por solicitud y garantiza su cierre."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
