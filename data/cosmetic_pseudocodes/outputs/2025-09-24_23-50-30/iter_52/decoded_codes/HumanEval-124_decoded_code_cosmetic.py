from typing import Tuple


def valid_date(delta_string: str) -> bool:
    def check_bounds(num: int, lower_bound: int, upper_bound: int) -> bool:
        return lower_bound <= num <= upper_bound

    def parse_components(drift: str) -> Tuple[str, str, str]:
        parts_list = drift.split('-')
        if len(parts_list) != 3:
            raise ValueError("Invalid date format")
        return parts_list[0], parts_list[1], parts_list[2]

    trimmed_str = delta_string.strip()

    try:
        m_str, d_str, y_str = parse_components(trimmed_str)
        month_val = int(m_str)
        day_val = int(d_str)
        year_val = int(y_str)
    except Exception:
        return False

    if not check_bounds(month_val, 1, 12):
        return False
    if month_val == 2 and not check_bounds(day_val, 1, 29):
        return False
    if month_val in {4, 6, 9, 11} and not check_bounds(day_val, 1, 30):
        return False
    if month_val in {1, 3, 5, 7, 8, 10, 12} and not check_bounds(day_val, 1, 31):
        return False

    return True