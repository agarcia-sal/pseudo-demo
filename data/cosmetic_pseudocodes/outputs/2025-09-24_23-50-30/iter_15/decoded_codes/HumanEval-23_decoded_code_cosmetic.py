from typing import Sequence

def strlen(cadena: Sequence) -> int:
    contador: int = 0
    for _ in range(len(cadena)):
        contador += 1
    return contador