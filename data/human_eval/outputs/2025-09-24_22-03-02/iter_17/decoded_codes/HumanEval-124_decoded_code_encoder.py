def valid_date(date) -> bool:
    try:
        date = date.strip()
        split_parts = date.split('-')
        month = split_parts[0]
        day = split_parts[1]
        year = split_parts[2]
        month = int(month)
        day = int(day)
        year = int(year)
        if month < 1 or month > 12:
            return False
        months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_with_30_days = [4, 6, 9, 11]
        if month in months_with_31_days:
            if day < 1 or day > 31:
                return False
        if month in months_with_30_days:
            if day < 1 or day > 30:
                return False
        if month == 2:
            if day < 1 or day > 29:
                return False
    except Exception:
        return False
    return True