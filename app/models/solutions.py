from typing import Optional, List, Literal
from pydantic import BaseModel, constr, validator

class Order (BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: Literal['completed', 'pending', 'canceled']

    @validator('price')
    def price_non_negative(cls, v):
        if v < 0:
            raise ValueError(f'El precio {v} no puede ser negativo')
        return v

class Orders (BaseModel):
    orders: List[Order]

class Criterion (BaseModel):
    criterion: Literal['completed', 'pending', 'canceled', 'all']
