from typing import List


def valid_date(date_string: str) -> bool:
    trimmed_date: str = date_string.strip()
    parts: List[str] = trimmed_date.split('-')

    if len(parts) != 3:
        return False

    m_str, d_str, y_str = parts

    try:
        m: int = int(m_str)
        d: int = int(d_str)
        y: int = int(y_str)
    except ValueError:
        return False

    if m < 1 or m > 12:
        return False

    if m in {1, 3, 5, 7, 8, 10, 12}:
        if d < 1 or d > 31:
            return False
    elif m in {4, 6, 9, 11}:
        if d < 1 or d > 30:
            return False
    elif m == 2:
        if d < 1 or d > 29:
            return False
    else:
        return False

    return True