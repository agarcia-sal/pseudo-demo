def valid_date(date) -> bool:
    try:
        date = date.strip()
        parts = date.split('-')
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
        if month < 1 or month > 12:
            return False
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (day < 1 or day > 31):
            return False
        if (month == 4 or month == 6 or month == 9 or month == 11) and (day < 1 or day > 30):
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
    except:
        return False
    return True