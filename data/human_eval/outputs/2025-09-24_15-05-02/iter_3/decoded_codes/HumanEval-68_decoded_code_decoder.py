def pluck(arr):
    if not arr:
        return []

    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []

    smallest_even = min(evens)
    index_of_smallest_even = arr.index(smallest_even)

    return [smallest_even, index_of_smallest_even]