def is_sorted(lst):
    from collections import Counter
    count_digit = Counter(lst)
    if any(count_digit[i] > 2 for i in lst):
        return False
    return all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))