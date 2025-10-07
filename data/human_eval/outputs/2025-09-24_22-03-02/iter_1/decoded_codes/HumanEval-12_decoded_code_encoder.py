def longest(strings):
    if not strings:
        return None
    max_len = max(len(x) for x in strings)
    for s in strings:
        if len(s) == max_len:
            return s