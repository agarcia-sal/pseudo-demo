def valid_date(d):
    try:
        m, day, y = map(int, d.strip().split('-'))
        if m < 1 or m > 12:
            return False
        if (m in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31)) or \
           (m in [4, 6, 9, 11] and (day < 1 or day > 30)) or \
           (m == 2 and (day < 1 or day > 29)):
            return False
    except:
        return False
    return True