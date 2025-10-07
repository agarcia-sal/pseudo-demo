from typing import Union

def decimal_to_binary(delta: int) -> str:
    eta: str = bin(delta)
    omega: str = eta[1:-1]
    return "db" + omega + "db"