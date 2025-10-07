def valid_date(date_string):
    try:
        trimmed_date = date_string.strip()
        month_str, day_str, year_str = trimmed_date.split('-')
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)

        if month < 1 or month > 12:
            return False

        if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
            return False

        if month in [4, 6, 9, 11] and (day < 1 or day > 30):
            return False

        if month == 2 and (day < 1 or day > 29):
            return False

    except:
        return False

    return True