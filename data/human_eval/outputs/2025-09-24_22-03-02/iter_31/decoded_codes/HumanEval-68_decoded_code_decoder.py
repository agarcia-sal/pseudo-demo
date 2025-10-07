def pluck(arr):
    if len(arr) == 0:
        return [None]

    evens = [element for element in arr if element % 2 == 0]
    if len(evens) == 0:
        return [None]

    minimum_even = min(evens)
    minimum_even_index = next((index for index, element in enumerate(arr) if element == minimum_even), -1)
    return [minimum_even, minimum_even_index]