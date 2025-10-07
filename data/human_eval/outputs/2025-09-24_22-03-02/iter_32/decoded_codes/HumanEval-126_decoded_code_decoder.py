def is_sorted(lst) -> bool:
    count_digit = {}
    index = 0
    while index < len(lst):
        element = lst[index]
        count_digit[element] = 0
        index += 1
    index = 0
    while index < len(lst):
        element = lst[index]
        count_digit[element] += 1
        index += 1
    index = 0
    while index < len(lst):
        element = lst[index]
        if count_digit[element] > 2:
            return False
        index += 1
    if len(lst) == 0 or len(lst) == 1:
        return True
    index = 1
    while index < len(lst):
        if lst[index - 1] > lst[index]:
            return False
        index += 1
    return True