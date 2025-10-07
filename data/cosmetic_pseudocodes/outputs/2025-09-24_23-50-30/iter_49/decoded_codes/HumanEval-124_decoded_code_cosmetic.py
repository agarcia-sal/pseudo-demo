from typing import Callable


def valid_date(alpha: str) -> bool:
    def process(epsilon: str) -> bool:
        if "-" in epsilon:
            q = epsilon.split("-")
            if len(q) == 3:
                u1, u2, u3 = q
                v1 = int(u1)
                v2 = int(u2)
                v3 = int(u3)  # Unused in validation but parsed as per pseudocode

                if not (1 <= v1 <= 12):
                    return False

                if v1 in {1, 3, 5, 7, 8, 10, 12}:
                    return 1 <= v2 <= 31
                elif v1 in {4, 6, 9, 11}:
                    return 1 <= v2 <= 30
                elif v1 == 2:
                    return 1 <= v2 <= 29
                else:
                    return False
            else:
                return False
        else:
            return False

    eta = alpha.strip()

    try:
        return process(eta)
    except Exception:
        return False