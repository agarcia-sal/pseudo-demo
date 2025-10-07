from typing import List

def decimal_to_binary(x1: int) -> str:
    x2: List[str] = []
    x3: List[str] = list(bin(x1))
    x4: List[str] = x3[2:]
    x2.append("db")
    x2.extend(x4)
    x2.append("db")
    return "".join(x2)