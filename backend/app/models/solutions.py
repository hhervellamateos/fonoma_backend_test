from typing import Optional, List, Literal
from pydantic import BaseModel, constr, validator

class Order (BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: Literal['completed', 'pending', 'canceled']

class Orders (BaseModel):
    orders: List[Order]

class Criterion (BaseModel):
    criterion: Literal['completed', 'pending', 'canceled', 'all']
