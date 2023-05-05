from models.solutions import OrderList
from typing import List, Optional
import json
from fastapi import Body

def say_hello(name: Optional[str] = None) -> str:
    msg = "Hello"
    if name:
        msg += f", {name}"

    return f"{msg} !!!"

def process_orders (order_list: OrderList = Body(...)) -> float:
    try:
        total = 0
        criterion = order_list.criterion
        for order in order_list.orders:
            if order.status == criterion or criterion == "all":
                total += order.price * order.quantity

        return round(total, 2)
    
    except Exception as e:
        raise NameError(str(e))