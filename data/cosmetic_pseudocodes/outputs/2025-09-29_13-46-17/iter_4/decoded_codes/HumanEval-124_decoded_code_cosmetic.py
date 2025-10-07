from typing import Callable


def valid_date(date_string: str) -> bool:
    def check_bounds(m: int, d: int) -> bool:
        if not (1 <= m <= 12):
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
        return True

    def parse_and_validate(str_input: str) -> bool:
        str_trimmed = str_input.strip()
        parts = str_trimmed.split("-")
        if len(parts) != 3:
            return False
        m_str, d_str, y_str = parts
        try:
            m_val = int(m_str)
            d_val = int(d_str)
            _ = int(y_str)  # y_val not used beyond parsing validation
        except ValueError:
            return False
        return check_bounds(m_val, d_val)

    return parse_and_validate(date_string)