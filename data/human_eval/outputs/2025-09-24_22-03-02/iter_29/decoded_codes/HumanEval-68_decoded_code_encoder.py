def pluck(arr):
    if len(arr) == 0:
        return [None]
    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return [None]
    minimum_value = evens[0]
    for v in evens[1:]:
        if v < minimum_value:
            minimum_value = v
    minimum_index = 0
    for i, val in enumerate(arr):
        if val == minimum_value:
            minimum_index = i
            break
    return [minimum_value, minimum_index]