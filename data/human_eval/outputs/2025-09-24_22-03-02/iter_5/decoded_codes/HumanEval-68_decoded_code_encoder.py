def pluck(arr):
    if len(arr) == 0:
        return []
    evens = [e for e in arr if e % 2 == 0]
    if not evens:
        return []
    smallest_even = min(evens)
    smallest_index = arr.index(smallest_even)
    return [smallest_even, smallest_index]