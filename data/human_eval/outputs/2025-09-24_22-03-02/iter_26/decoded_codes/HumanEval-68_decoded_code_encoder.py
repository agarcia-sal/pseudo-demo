def pluck(arr):
    if len(arr) == 0:
        return []

    evens = [element for element in arr if element % 2 == 0]

    if len(evens) == 0:
        return []

    smallest_even = evens[0]
    for current in evens[1:]:
        if current < smallest_even:
            smallest_even = current

    smallest_index = -1
    for index, element in enumerate(arr):
        if element == smallest_even:
            smallest_index = index
            break

    result = []
    result.append(smallest_even)
    result.append(smallest_index)
    return result