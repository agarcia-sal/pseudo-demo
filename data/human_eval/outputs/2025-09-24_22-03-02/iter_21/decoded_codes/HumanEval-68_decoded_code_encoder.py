def pluck(arr):
    if len(arr) == 0:
        return [None]
    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return [None]
    minimum_even = evens[0]
    for i in range(1, len(evens)):
        if evens[i] < minimum_even:
            minimum_even = evens[i]
    minimum_index = 0
    for j in range(len(arr)):
        if arr[j] == minimum_even:
            minimum_index = j
            break
    return [minimum_even, minimum_index]