def valid_date(date) -> bool:
    try:
        date = date.strip()
        split_date = date.split('-')
        month = int(split_date[0])
        day = int(split_date[1])
        year = int(split_date[2])
        if month < 1 or month > 12:
            return False
        allowed_months_31 = [1,3,5,7,8,10,12]
        allowed_months_30 = [4,6,9,11]
        if month in allowed_months_31 and (day < 1 or day > 31):
            return False
        if month in allowed_months_30 and (day < 1 or day > 30):
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
    except:
        return False
    return True