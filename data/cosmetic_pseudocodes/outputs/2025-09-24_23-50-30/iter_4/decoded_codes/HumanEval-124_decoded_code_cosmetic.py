from typing import Callable


def valid_date(input_string: str) -> bool:
    def check_range(value: int, minimum: int, maximum: int) -> bool:
        return minimum <= value <= maximum

    def valid_day(m: int, d: int) -> bool:
        if m in {1, 3, 5, 7, 8, 10, 12}:
            return check_range(d, 1, 31)
        if m in {4, 6, 9, 11}:
            return check_range(d, 1, 30)
        if m == 2:
            return check_range(d, 1, 29)
        return False

    try:
        trimmed = input_string.strip()
        parts = trimmed.split('-')
        if len(parts) != 3:
            return False

        m_str, d_str, y_str = parts
        m = int(m_str)
        d = int(d_str)
        y = int(y_str)

        if not check_range(m, 1, 12):
            return False
        if not valid_day(m, d):
            return False

    except Exception:
        return False

    return True