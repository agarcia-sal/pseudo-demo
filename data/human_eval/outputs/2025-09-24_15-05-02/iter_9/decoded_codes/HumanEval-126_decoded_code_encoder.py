from collections import defaultdict

def is_sorted(lst):
    count_digit = defaultdict(int)
    for element in lst:
        count_digit[element] += 1
    if any(count_digit[element] > 2 for element in lst):
        return False
    return all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))