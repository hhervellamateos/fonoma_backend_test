from models.solutions import Orders, Criterion
from typing import List, Optional
import json

def say_hello(name: Optional[str] = None) -> str:
    msg = "Hello"
    if name:
        msg += f", {name}"

    return f"{msg} !!!"

def process_orders (orders: Orders, criterion: str) -> float:
    print(criterion)
    try:
        total = 0
        for order in orders.orders:
            if order.status == criterion or criterion == "all":
                total += order.price

        return round(total, 2)
    
    except Exception as e:
        raise NameError(str(e))