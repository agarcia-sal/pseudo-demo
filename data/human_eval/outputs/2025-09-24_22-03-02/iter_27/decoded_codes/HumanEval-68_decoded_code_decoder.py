def pluck(arr):
    if len(arr) == 0:
        return []
    evens = []
    for i in range(len(arr)):
        x = arr[i]
        if x % 2 == 0:
            evens.append(x)
    if len(evens) == 0:
        return []
    smallest_even = evens[0]
    for j in range(1, len(evens)):
        if evens[j] < smallest_even:
            smallest_even = evens[j]
    smallest_index = 0
    for k in range(len(arr)):
        if arr[k] == smallest_even:
            smallest_index = k
            break
    return [smallest_even, smallest_index]