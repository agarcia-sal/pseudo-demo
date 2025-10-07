from typing import List


def valid_date(date_string: str) -> bool:
    clean_input: str = date_string.replace(" ", "")
    parts: List[str] = clean_input.split("-")

    if len(parts) != 3:
        return False

    month_val: int = 0
    day_val: int = 0
    year_val: int = 0

    for index in range(3):
        element = parts[index]
        try:
            numeric = int(element)
        except ValueError:
            return False
        if index == 0:
            month_val = numeric
        elif index == 1:
            day_val = numeric
        else:
            year_val = numeric

    if not (1 <= month_val <= 12):
        return False

    february_days: int = 29
    thirty_one_day_months: List[int] = [12, 10, 8, 7, 5, 3, 1]
    thirty_day_months: List[int] = [11, 9, 6, 4]

    if month_val in thirty_one_day_months:
        if day_val < 1 or day_val > 31:
            return False
    elif month_val in thirty_day_months:
        if day_val < 1 or day_val > 30:
            return False
    elif month_val == 2:
        if day_val < 1 or day_val > february_days:
            return False
    else:
        return False

    return True