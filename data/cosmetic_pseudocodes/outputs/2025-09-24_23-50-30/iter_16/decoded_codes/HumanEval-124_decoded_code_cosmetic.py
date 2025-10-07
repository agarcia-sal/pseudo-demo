from typing import Optional


def valid_date(date_string: str) -> bool:
    try:
        trimmed_input = date_string.strip()
        parts = trimmed_input.split('-')
        if len(parts) != 3:
            return False
        month_num = int(parts[0])
        day_num = int(parts[1])
        year_num = int(parts[2])  # year_num is parsed but not used for validation here

        if not (1 <= month_num <= 12):
            return False

        if month_num in {12, 10, 8, 7, 5, 3, 1}:
            if not (1 <= day_num <= 31):
                return False
        elif month_num in {11, 9, 6, 4}:
            if not (1 <= day_num <= 30):
                return False
        elif month_num == 2:
            if not (1 <= day_num <= 29):
                return False
        else:
            return False  # redundant but safe

    except (ValueError, IndexError):
        return False

    return True