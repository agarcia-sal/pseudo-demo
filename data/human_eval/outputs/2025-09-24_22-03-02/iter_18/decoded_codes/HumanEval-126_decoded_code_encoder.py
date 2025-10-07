def is_sorted(lst) -> bool:
    count_digit = {}
    for element in lst:
        if element not in count_digit:
            count_digit[element] = 0
    for element in lst:
        count_digit[element] += 1
    for element in lst:
        if count_digit[element] > 2:
            return False
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True