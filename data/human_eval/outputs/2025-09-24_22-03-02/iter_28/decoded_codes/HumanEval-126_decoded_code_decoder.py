def is_sorted(lst) -> bool:
    count_digit = {}
    for i in range(len(lst)):
        count_digit[lst[i]] = 0
    for i_index in range(len(lst)):
        i = lst[i_index]
        count_digit[i] += 1
    for i_index in range(len(lst)):
        i = lst[i_index]
        if count_digit[i] > 2:
            return False
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True