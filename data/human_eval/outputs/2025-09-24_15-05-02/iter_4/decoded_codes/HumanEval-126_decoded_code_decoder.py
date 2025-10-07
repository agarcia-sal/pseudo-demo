from collections import defaultdict

def is_sorted(lst):
    count_digit = defaultdict(int)

    for element in lst:
        count_digit[element] += 1

    for element in lst:
        if count_digit[element] > 2:
            return False

    for index in range(1, len(lst)):
        if lst[index - 1] > lst[index]:
            return False

    return True