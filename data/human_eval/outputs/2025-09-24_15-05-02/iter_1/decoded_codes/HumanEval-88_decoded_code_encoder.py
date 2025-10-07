def sort_array(a):
    if len(a) == 0:
        return []
    reverse = ((a[0] + a[-1]) % 2 == 0)
    return sorted(a, reverse=reverse)