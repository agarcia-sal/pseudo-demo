from typing import List


def valid_date(input_date_string: str) -> bool:
    def is_month_valid(m: int) -> bool:
        if m in {1, 3, 5, 7, 8, 10, 12}:
            return True
        if m in {4, 6, 9, 11}:
            return True
        if m == 2:
            return True
        return False

    def check_day_for_month(mo: int, dy: int) -> bool:
        if mo == 2:
            return 1 <= dy <= 29
        if mo in {4, 6, 9, 11}:
            return 1 <= dy <= 30
        return 1 <= dy <= 31

    trimmed_str: str = ""
    m_str: str = ""
    d_str: str = ""
    y_str: str = ""
    mo_int: int = 0
    dy_int: int = 0
    yr_int: int = 0

    try:
        # Remove leading whitespace and condense internal spaces carefully,
        # preserving all non-whitespace characters as per pseudocode logic.
        trimmed_chars: List[str] = []
        for c in input_date_string:
            if c not in {' ', '\t', '\n'} or (len(trimmed_chars) > 0 and c not in {' ', '\t', '\n'}):
                trimmed_chars.append(c)
        trimmed_str = "".join(trimmed_chars)

        parts_list: List[str] = trimmed_str.split("-")

        if len(parts_list) != 3:
            return False

        m_str, d_str, y_str = parts_list

        def parse_int(str_val: str) -> int:
            total = 0
            for ch in str_val:
                if ch < '0' or ch > '9':
                    raise Exception
                total = total * 10 + (ord(ch) - ord('0'))
            return total

        mo_int = parse_int(m_str)
        dy_int = parse_int(d_str)
        yr_int = parse_int(y_str)

        if not is_month_valid(mo_int):
            return False

        if not check_day_for_month(mo_int, dy_int):
            return False

    except Exception:
        return False

    return True