def valid_date(date_string: str) -> bool:
    try:
        trimmed_date = date_string.strip()
        month_string, day_string, year_string = trimmed_date.split('-')
        month, day, year = int(month_string), int(day_string), int(year_string)

        if month < 1 or month > 12:
            return False

        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False

        if month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False

        if month == 2:
            if day < 1 or day > 29:
                return False

    except Exception:
        return False

    return True