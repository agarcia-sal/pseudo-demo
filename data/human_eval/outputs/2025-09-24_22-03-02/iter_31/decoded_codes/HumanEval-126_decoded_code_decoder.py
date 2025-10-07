def is_sorted(lst):
    count_digit = {}
    for key in lst:
        count_digit[key] = 0
    for key in lst:
        count_digit[key] += 1
    for key in lst:
        if count_digit[key] > 2:
            return False
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            return False
    return True