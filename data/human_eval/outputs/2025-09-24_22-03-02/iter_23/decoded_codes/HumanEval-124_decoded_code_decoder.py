def valid_date(date: str) -> bool:
    try:
        date = date.strip()
        splitted = date.split('-')
        month_string = splitted[0]
        day_string = splitted[1]
        year_string = splitted[2]
        month = int(month_string)
        day = int(day_string)
        year = int(year_string)
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
    except:
        return False
    return True