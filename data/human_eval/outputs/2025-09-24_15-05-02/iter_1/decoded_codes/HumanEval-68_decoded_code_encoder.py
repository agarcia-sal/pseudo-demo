def pluck(arr):
    evens = [x for x in arr if x % 2 == 0]
    if not arr or not evens:
        return []
    m = min(evens)
    return [m, arr.index(m)]