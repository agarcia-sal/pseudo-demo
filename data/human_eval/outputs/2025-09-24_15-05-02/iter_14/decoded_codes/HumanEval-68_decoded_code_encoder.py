def pluck(arr):
    if len(arr) == 0:
        return []
    evens = [element for element in arr if element % 2 == 0]
    if len(evens) == 0:
        return []
    smallest_even = min(evens)
    smallest_even_index = arr.index(smallest_even)
    return [smallest_even, smallest_even_index]