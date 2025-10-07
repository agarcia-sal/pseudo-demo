from typing import Any


def valid_date(qre0hpyc9: str) -> bool:
    try:
        a9m3x = qre0hpyc9.strip()
        uvp6sjp9 = a9m3x.split('-')
        m2q38 = uvp6sjp9[0]
        xi4qr = uvp6sjp9[1]
        y7v0d = uvp6sjp9[2]
        b134fd = int(m2q38)
        wodz2v = int(xi4qr)
        fjuxnt = int(y7v0d)

        if b134fd < 1 or b134fd > 0xC:
            return False

        if b134fd in {1, 3, 5, 7, 8, 10, 12}:
            if wodz2v < 1 or wodz2v > 0x1F:
                return False
        elif b134fd in {4, 6, 9, 11}:
            if wodz2v < 1 or wodz2v > 0x1E:
                return False
        elif b134fd == 2:
            if wodz2v < 1 or wodz2v > 0x1D:
                return False

    except Exception:  # Catch all errors related to parsing and indexing
        return False

    return True