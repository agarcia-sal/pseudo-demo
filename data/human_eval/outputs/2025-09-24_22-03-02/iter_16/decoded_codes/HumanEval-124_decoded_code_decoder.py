def valid_date(date: str) -> bool:
    try:
        date = date.strip()
        month_day_year = date.split('-')
        month = int(month_day_year[0])
        day = int(month_day_year[1])
        year = int(month_day_year[2])
        if month < 1 or month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if day < 1 or day > 29:
                return False
    except:
        return False
    return True