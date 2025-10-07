from typing import Callable

def valid_date(aux0: str) -> bool:
    aux1: str = aux0.strip()
    aux2: str
    aux3: str
    aux4: str
    aux5: int
    aux6: int
    aux7: int

    def aux8() -> bool:
        nonlocal aux2, aux3, aux4, aux5, aux6, aux7
        try:
            aux2, aux3, aux4 = aux1.split('-')
            aux5 = int(aux2)
            aux6 = int(aux3)
            aux7 = int(aux4)

            if aux5 < 1:
                return False
            if aux5 > 12:
                return False
            if aux5 == 2:
                if aux6 < 1 or aux6 > 29:
                    return False
            elif aux5 in {4, 6, 9, 11}:
                if aux6 < 1 or aux6 > 30:
                    return False
            elif aux5 in {1, 3, 5, 7, 8, 10, 12}:
                if aux6 < 1 or aux6 > 31:
                    return False

            return True
        except Exception:
            return False

    return aux8()