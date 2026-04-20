from datetime import datetime

from pydantic import BaseModel, Field


class DishOut(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float

    class Config:
        from_attributes = True


class OrderItemCreate(BaseModel):
    dish_id: int
    quantity: int = Field(ge=1)


class OrderCreate(BaseModel):
    items: list[OrderItemCreate]


class OrderItemOut(BaseModel):
    dish_id: int
    dish_name: str
    quantity: int
    unit_price: float
    line_total: float


class OrderOut(BaseModel):
    id: int
    status: str
    subtotal: float
    total: float
    created_at: datetime
    items: list[OrderItemOut]


class PaymentCreate(BaseModel):
    method: str = Field(pattern="^(cash|card)$")
    amount_paid: float = Field(gt=0)


class PaymentOut(BaseModel):
    id: int
    order_id: int
    method: str
    amount_paid: float
    change_amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
