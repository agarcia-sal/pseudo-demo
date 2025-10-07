from collections import Counter

def is_sorted(lst):
    cnt = Counter(lst)
    if any(count > 2 for count in cnt.values()):
        return False
    return all(lst[i-1] <= lst[i] for i in range(1, len(lst)))