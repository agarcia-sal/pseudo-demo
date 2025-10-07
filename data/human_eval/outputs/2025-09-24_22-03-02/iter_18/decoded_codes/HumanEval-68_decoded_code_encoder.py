def pluck(arr):
    if len(arr) == 0:
        return [None]
    evens = [v for v in arr if v % 2 == 0]
    if len(evens) == 0:
        return [None]
    min_even = evens[0]
    for i in range(1, len(evens)):
        if evens[i] < min_even:
            min_even = evens[i]
    min_index = -1
    for j in range(len(arr)):
        if arr[j] == min_even:
            min_index = j
            break
    return [min_even, min_index]