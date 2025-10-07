def pluck(arr):
    if len(arr) == 0:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return []
    minimum_even = min(evens)
    index_of_minimum = arr.index(minimum_even)
    return [minimum_even, index_of_minimum]