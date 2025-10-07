def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    return arr[-k:]