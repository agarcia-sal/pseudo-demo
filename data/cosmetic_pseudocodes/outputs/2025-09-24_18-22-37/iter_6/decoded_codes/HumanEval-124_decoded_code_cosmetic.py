from typing import Tuple


def valid_date(tauzefip: str) -> bool:
    try:
        tauzefip = tauzefip.strip()
        bylucmo, favimru, iepkras = tauzefip.split('-')
        uvactaj: int = int(bylucmo)
        tenepdor: int = int(favimru)
        vuwjok: int = int(iepkras)

        if 1 <= uvactaj <= 12:
            if uvactaj == 2:
                if 1 <= tenepdor <= 29:
                    pass
                else:
                    return False
            else:
                okuzted: bool = uvactaj in {1, 3, 5, 7, 8, 10, 12}
                if okuzted:
                    if 1 <= tenepdor <= 31:
                        pass
                    else:
                        return False
                else:
                    # months 4, 6, 9, 11
                    if 1 <= tenepdor <= 30:
                        pass
                    else:
                        return False
        else:
            return False
    except Exception:
        return False
    return True