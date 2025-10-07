def pluck(arr):
    if len(arr) == 0:
        return []

    evens = []
    for x in arr:
        if x % 2 == 0:
            evens.append(x)

    if len(evens) == 0:
        return []

    smallest_even = min(evens)
    smallest_index = arr.index(smallest_even)

    return [smallest_even, smallest_index]