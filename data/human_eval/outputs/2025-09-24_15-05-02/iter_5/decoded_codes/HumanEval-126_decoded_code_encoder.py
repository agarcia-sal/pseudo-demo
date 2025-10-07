from collections import defaultdict

def is_sorted(lst):
    count_digit = defaultdict(int)
    for element in lst:
        count_digit[element] += 1

    if any(count_digit[element] > 2 for element in lst):
        return False

    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False

    return True