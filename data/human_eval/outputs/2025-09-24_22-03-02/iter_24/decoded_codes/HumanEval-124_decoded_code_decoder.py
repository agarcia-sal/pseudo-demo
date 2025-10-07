def valid_date(date) -> bool:
    try:
        date = date.strip()
        split_result = date.split('-')
        month = int(split_result[0])
        day = int(split_result[1])
        year = int(split_result[2])
        if month < 1 or month > 12:
            return False
        month_list_31 = [1, 3, 5, 7, 8, 10, 12]
        month_list_30 = [4, 6, 9, 11]
        if month in month_list_31:
            if day < 1 or day > 31:
                return False
        if month in month_list_30:
            if day < 1 or day > 30:
                return False
        if month == 2:
            if day < 1 or day > 29:
                return False
    except:
        return False
    return True