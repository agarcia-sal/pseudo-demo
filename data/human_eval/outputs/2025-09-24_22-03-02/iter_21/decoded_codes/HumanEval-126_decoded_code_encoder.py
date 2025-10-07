def is_sorted(lst) -> bool:
    count_digit = {}
    for i in range(len(lst)):
        count_digit[lst[i]] = 0
    for i in range(len(lst)):
        count_digit[lst[i]] += 1
    for i in range(len(lst)):
        if count_digit[lst[i]] > 2:
            return False
    sorted_flag = True
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            sorted_flag = False
            break
    return sorted_flag