from typing import Any


def valid_date(alpha: str) -> bool:
    try:
        alpha = alpha.strip()
        parts = alpha.split("-")
        if len(parts) != 3:
            return False

        x1 = parts[0]
        x2 = parts[1]
        x3 = parts[2]

        m_x = int(x1)
        d_x = int(x2)
        y_x = int(x3)

        if m_x < 1 or m_x > 12:
            return False

        if m_x == 2:
            if d_x < 1 or d_x > 29:
                return False
        else:
            if m_x in {4, 6, 9, 11}:
                if d_x < 1 or d_x > 30:
                    return False
            else:
                if d_x < 1 or d_x > 31:
                    return False
    except Exception:
        return False
    return True