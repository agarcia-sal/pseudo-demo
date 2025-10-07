from typing import List


def valid_date(date_string: str) -> bool:
    def check_bounds(m_val: int, d_val: int) -> bool:
        # Check month and day ranges per calendar rules, allowing February up to day 29 inclusively
        if not (1 <= m_val <= 12):
            return False
        if m_val in {1, 3, 5, 7, 8, 10, 12}:
            return 1 <= d_val <= 31
        if m_val in {4, 6, 9, 11}:
            return 1 <= d_val <= 30
        if m_val == 2:
            return 1 <= d_val <= 29
        return False

    try:
        trimmed_str = date_string.strip()
        parts_list: List[str] = trimmed_str.split('-')
        if len(parts_list) != 3:
            return False

        m_str, d_str, y_str = parts_list
        m_val = int(m_str)
        d_val = int(d_str)
        y_val = int(y_str)  # y_val parsed but unused per pseudocode, keep for completeness

        return check_bounds(m_val, d_val)
    except Exception:
        return False