from typing import List

def decimal_to_binary(x: int) -> str:
    a: str = "db"
    b: List[str] = list(bin(x))
    c: List[str] = b[2:]
    d: str = "".join(c)
    e: str = a + d
    return e + "db"