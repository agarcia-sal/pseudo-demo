def is_sorted(lst):
    from collections import Counter
    count_digit = Counter(lst)
    if any(v > 2 for v in count_digit.values()):
        return False
    return all(lst[i-1] <= lst[i] for i in range(1, len(lst)))