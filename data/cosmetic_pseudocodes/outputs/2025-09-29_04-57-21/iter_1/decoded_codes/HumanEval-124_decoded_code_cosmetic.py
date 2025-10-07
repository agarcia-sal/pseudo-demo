from typing import Any


def valid_date(date_string: str) -> bool:
    try:
        trimmed_date = date_string.strip()
        parts = trimmed_date.split('-')
        if len(parts) != 3:
            return False
        m_str, d_str, y_str = parts
        m = int(m_str)
        d = int(d_str)
        y = int(y_str)

        if not (1 <= m <= 12):
            return False

        if m == 2:
            if d < 1 or d > 29:
                return False
        elif m in {4, 6, 9, 11}:
            if d < 1 or d > 30:
                return False
        elif m in {1, 3, 5, 7, 8, 10, 12}:
            if d < 1 or d > 31:
                return False
        else:
            # Defensive: should not happen due to prior check, but keeps logic clear.
            return False

    except Exception:
        return False

    return True