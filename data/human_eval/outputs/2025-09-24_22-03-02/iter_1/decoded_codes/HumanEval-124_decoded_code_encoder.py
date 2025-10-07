def valid_date(date):
    if not date:
        return False
    try:
        m, d, y = date.split('-')
        m, d, y = int(m), int(d), int(y)
    except:
        return False
    if not (1 <= m <= 12):
        return False
    if (m in [1, 3, 5, 7, 8, 10, 12] and not (1 <= d <= 31)) or \
       (m in [4, 6, 9, 11] and not (1 <= d <= 30)) or \
       (m == 2 and not (1 <= d <= 29)):
        return False
    return True