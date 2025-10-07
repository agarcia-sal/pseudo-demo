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

    index_of_minimum = -1
    for i in range(len(arr)):
        if arr[i] == minimum_even:
            index_of_minimum = i
            break

    return [minimum_even, index_of_minimum]