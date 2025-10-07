def pluck(arr):
    if len(arr) == 0:
        return []
    evens = []
    index = 0
    while index < len(arr):
        if arr[index] % 2 == 0:
            evens.append(arr[index])
        index += 1
    if len(evens) == 0:
        return []
    min_even = evens[0]
    i = 1
    while i < len(evens):
        if evens[i] < min_even:
            min_even = evens[i]
        i += 1
    min_index = 0
    j = 0
    while j < len(arr):
        if arr[j] == min_even:
            min_index = j
            break
        j += 1
    return [min_even, min_index]