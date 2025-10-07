def is_sorted(lst) -> bool:
    count_digit = {}
    for i in range(len(lst)):
        key = lst[i]
        count_digit[key] = 0

    for j in range(len(lst)):
        key = lst[j]
        count_digit[key] += 1

    duplicate_over_two = False
    for k in range(len(lst)):
        key = lst[k]
        if count_digit[key] > 2:
            duplicate_over_two = True
            break

    if duplicate_over_two == True:
        return False

    is_ascending = True
    for m in range(1, len(lst)):
        if lst[m - 1] > lst[m]:
            is_ascending = False
            break

    if is_ascending == True:
        return True
    else:
        return False