"""Esquemas Pydantic usados por la API para validar entradas y serializar salidas."""

from datetime import datetime

from pydantic import BaseModel, Field


class DishOut(BaseModel):
    """Representacion publica de un plato activo."""
    id: int
    name: str
    category: str
    description: str
    price: float

    class Config:
        from_attributes = True


class OrderItemCreate(BaseModel):
    """Payload de entrada para un plato solicitado dentro de un pedido."""
    dish_id: int
    quantity: int = Field(ge=1)


class OrderCreate(BaseModel):
    """Payload de entrada para crear un pedido completo."""
    items: list[OrderItemCreate]


class OrderItemOut(BaseModel):
    """Linea serializada que se devuelve dentro de un pedido."""
    dish_id: int
    dish_name: str
    quantity: int
    unit_price: float
    line_total: float


class OrderOut(BaseModel):
    """Pedido serializado con totales calculados y lineas."""
    id: int
    status: str
    subtotal: float
    total: float
    created_at: datetime
    items: list[OrderItemOut]


class PaymentCreate(BaseModel):
    """Payload de entrada usado para procesar una operacion de pago."""
    method: str = Field(pattern="^(cash|card)$")
    amount_paid: float = Field(gt=0)


class PaymentOut(BaseModel):
    """Respuesta de pago serializada que devuelve la API."""
    id: int
    order_id: int
    method: str
    amount_paid: float
    change_amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
