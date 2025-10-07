def remove_duplicates(numbers):
    import collections
    c = collections.Counter(numbers)
    result = []
    for n in numbers:
        if c[n] <= 1:
            result.append(n)
    return result