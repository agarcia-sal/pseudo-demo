from typing import Literal


def valid_date(date_string: str) -> bool:
    try:
        input_trimmed = date_string.strip()
        part_month, part_day, part_year = input_trimmed.split('-', 2)
        num_month = int(part_month)
        num_day = int(part_day)
        _ = int(part_year)  # year parsed but unused in logic

        if not (1 <= num_month <= 12):
            return False

        if num_month in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= num_day <= 31):
                return False
        elif num_month in {4, 6, 9, 11}:
            if not (1 <= num_day <= 30):
                return False
        elif num_month == 2:
            if not (1 <= num_day <= 29):
                return False
        else:
            # Defensive fallback though unreachable due to prior range check
            return False
    except Exception:
        return False

    return True