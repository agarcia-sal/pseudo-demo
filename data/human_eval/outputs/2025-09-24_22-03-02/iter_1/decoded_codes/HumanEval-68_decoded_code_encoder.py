def pluck(arr):
    if not arr or all(x % 2 != 0 for x in arr):
        return []
    ev = [x for x in arr if x % 2 == 0]
    m = min(ev)
    return [m, arr.index(m)]