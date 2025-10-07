def is_sorted(lst) -> bool:
    count_digit = {}
    for element in lst:
        count_digit[element] = 0
    for element in lst:
        count_digit[element] += 1
    for element in lst:
        if count_digit[element] > 2:
            return False
    is_non_decreasing = True
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            is_non_decreasing = False
            break
    return is_non_decreasing