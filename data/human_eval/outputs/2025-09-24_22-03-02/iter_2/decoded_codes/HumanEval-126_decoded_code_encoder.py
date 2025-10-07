def is_sorted(lst):
    count_digit = {i: 0 for i in lst}

    for i in lst:
        count_digit[i] += 1

    for i in lst:
        if count_digit[i] > 2:
            return False

    for index in range(1, len(lst)):
        if lst[index - 1] > lst[index]:
            return False

    return True