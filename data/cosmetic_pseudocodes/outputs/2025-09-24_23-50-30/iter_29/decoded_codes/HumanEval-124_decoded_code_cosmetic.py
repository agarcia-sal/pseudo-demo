from typing import Any


def valid_date(input_str: str) -> bool:
    try:
        trimmed_str: str = input_str.strip()
        parts: list[str] = trimmed_str.split('-')
        if len(parts) != 3:
            return False
        m_s, d_s, y_s = parts

        m: int = int(m_s)
        d: int = int(d_s)
        y: int = int(y_s)

        if not (1 <= m <= 12):
            return False

        if m in {1, 3, 5, 7, 8, 10, 12} and not (1 <= d <= 31):
            return False

        if m in {4, 6, 9, 11} and not (1 <= d <= 30):
            return False

        if m == 2 and not (1 <= d <= 29):
            return False

    except Exception:  # catch all errors including index, conversion errors
        return False

    return True