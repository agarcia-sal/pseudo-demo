def histogram(test):
    list1 = test.split()
    if not list1:
        return {}
    from collections import Counter
    counts = Counter(list1)
    t = max(counts.values())
    return {k: t for k, v in counts.items() if v == t}