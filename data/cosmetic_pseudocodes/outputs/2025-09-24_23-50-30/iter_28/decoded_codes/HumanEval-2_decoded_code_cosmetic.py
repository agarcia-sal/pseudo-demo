from math import floor

def truncate_number(qr: float) -> float:
    zn: float = qr - floor(qr)
    return zn