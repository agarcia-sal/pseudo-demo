def pluck(arr):
    if len(arr) == 0:
        return ['EMPTY']
    evens = [x for x in arr if x % 2 == 0]
    if len(evens) == 0:
        return ['EMPTY']
    min_even = min(evens)
    min_even_index = next(i for i, v in enumerate(arr) if v == min_even)
    return [min_even, min_even_index]