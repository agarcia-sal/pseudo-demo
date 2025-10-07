from typing import List


def is_nested(cadena: str) -> bool:
    apertura: List[int] = []
    cierre: List[int] = []
    i: int = 0
    while i < len(cadena):
        if cadena[i] == '[':
            apertura.append(i)
        else:
            cierre.append(i)
        i += 1

    cierre.reverse()

    cantidad: int = 0
    indice_apertura: int = 0
    total_cierre: int = len(cierre)

    while indice_apertura < len(apertura):
        if indice_apertura < total_cierre and apertura[indice_apertura] < cierre[indice_apertura]:
            cantidad += 1
            indice_apertura += 1
        else:
            indice_apertura += 1

    return cantidad >= 2