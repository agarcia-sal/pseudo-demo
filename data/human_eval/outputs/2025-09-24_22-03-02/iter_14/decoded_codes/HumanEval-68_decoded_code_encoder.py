def pluck(arr):
    if len(arr) == 0:
        return [None]
    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return [None]
    smallest_even = min(evens)
    smallest_index = arr.index(smallest_even)
    return [smallest_even, smallest_index]