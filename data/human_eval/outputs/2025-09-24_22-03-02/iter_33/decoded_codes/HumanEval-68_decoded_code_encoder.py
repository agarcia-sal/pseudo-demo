def pluck(arr):
    if len(arr) == 0:
        return [None]
    evens = []
    for element in arr:
        if element % 2 == 0:
            evens.append(element)
    if len(evens) == 0:
        return [None]
    minimum_even = evens[0]
    for e in evens[1:]:
        if e < minimum_even:
            minimum_even = e
    minimum_index = 0
    found = False
    for i, val in enumerate(arr):
        if val == minimum_even and not found:
            minimum_index = i
            found = True
    return [minimum_even, minimum_index]