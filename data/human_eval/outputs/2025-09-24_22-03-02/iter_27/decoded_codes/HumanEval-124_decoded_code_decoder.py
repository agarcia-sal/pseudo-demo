def valid_date(date) -> bool:
    try:
        date = date.strip()
        temp_list = date.split('-')
        month = int(temp_list[0])
        day = int(temp_list[1])
        year = int(temp_list[2])
        if month < 1 or month > 12:
            return False
        allowed_months_31 = [1, 3, 5, 7, 8, 10, 12]
        allowed_months_30 = [4, 6, 9, 11]
        index_31 = 0
        while index_31 < len(allowed_months_31):
            if month == allowed_months_31[index_31]:
                if day < 1 or day > 31:
                    return False
            index_31 += 1
        index_30 = 0
        while index_30 < len(allowed_months_30):
            if month == allowed_months_30[index_30]:
                if day < 1 or day > 30:
                    return False
            index_30 += 1
        if month == 2:
            if day < 1 or day > 29:
                return False
    except:
        return False
    return True