from typing import Any


def valid_date(date: Any) -> bool:
    try:
        date = date.strip()
        parts = date.split('-')
        month_str = parts[0]
        day_str = parts[1]
        year_str = parts[2]
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
        if month < 1 or month > 12:
            return False
        long_months = [1, 3, 5, 7, 8, 10, 12]
        short_months = [4, 6, 9, 11]
        is_long_month = False
        for i in range(len(long_months)):
            if month == long_months[i]:
                is_long_month = True
                break
        is_short_month = False
        for i in range(len(short_months)):
            if month == short_months[i]:
                is_short_month = True
                break
        if is_long_month and (day < 1 or day > 31):
            return False
        if is_short_month and (day < 1 or day > 30):
            return False
        if month == 2 and (day < 1 or day > 29):
            return False
    except:
        return False
    return True