def valid_date(date) -> bool:
    try:
        date = date.strip()
        split_date = date.split('-')
        month_string = split_date[0]
        day_string = split_date[1]
        year_string = split_date[2]
        month = int(month_string)
        day = int(day_string)
        year = int(year_string)
        if month < 1 or month > 12:
            return False
        list_seven_months = [1, 3, 5, 7, 8, 10, 12]
        if month in list_seven_months and (day < 1 or day > 31):
            return False
        list_four_months = [4, 6, 9, 11]
        if month in list_four_months and (day < 1 or day > 30):
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
    except:
        return False
    return True