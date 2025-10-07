from typing import Optional

def valid_date(date_string: str) -> bool:
    try:
        trimmed_date = date_string.strip()
        month_string, day_string, year_string = trimmed_date.split('-')
        month = int(month_string)
        day = int(day_string)
        # year is parsed but not used for validation as per pseudocode
        _ = int(year_string)

        if not 1 <= month <= 12:
            return False
        if month in {1, 3, 5, 7, 8, 10, 12}:
            if not 1 <= day <= 31:
                return False
        elif month in {4, 6, 9, 11}:
            if not 1 <= day <= 30:
                return False
        elif month == 2:
            if not 1 <= day <= 29:
                return False
        else:
            return False
    except Exception:
        return False

    return True