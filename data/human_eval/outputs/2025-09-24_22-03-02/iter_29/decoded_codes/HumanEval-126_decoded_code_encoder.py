def is_sorted(lst) -> bool:
    count_digit = {}
    for i in range(len(lst)):
        key = lst[i]
        if key not in count_digit:
            count_digit[key] = 0
    for i in range(len(lst)):
        key = lst[i]
        count_digit[key] += 1
    for i in range(len(lst)):
        key = lst[i]
        if count_digit[key] > 2:
            return False
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True