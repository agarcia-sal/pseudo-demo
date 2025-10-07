def valid_date(date) -> bool:
    try:
        date = date.strip()
        parts = date.split('-')
        if len(parts) != 3:
            return False
        month_string = parts[0]
        day_string = parts[1]
        year_string = parts[2]
        month = int(month_string)
        day = int(day_string)
        year = int(year_string)
        if month < 1 or month > 12:
            return False
        months_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_30_days = [4, 6, 9, 11]
        is_month_31_days = False
        for index in range(len(months_31_days)):
            if month == months_31_days[index]:
                is_month_31_days = True
                break
        if is_month_31_days:
            if day < 1 or day > 31:
                return False
        else:
            is_month_30_days = False
            for index in range(len(months_30_days)):
                if month == months_30_days[index]:
                    is_month_30_days = True
                    break
            if is_month_30_days:
                if day < 1 or day > 30:
                    return False
            else:
                if month == 2:
                    if day < 1 or day > 29:
                        return False
    except:
        return False
    return True