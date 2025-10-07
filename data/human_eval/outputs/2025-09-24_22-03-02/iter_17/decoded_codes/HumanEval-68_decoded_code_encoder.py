def pluck(arr):
    if len(arr) == 0:
        return []
    evens = [element for element in arr if element % 2 == 0]
    if len(evens) == 0:
        return []
    minimum_even = evens[0]
    for even_element in evens:
        if even_element < minimum_even:
            minimum_even = even_element
    index_of_minimum = 0
    position = 0
    for element in arr:
        if element == minimum_even:
            index_of_minimum = position
            break
        position += 1
    return [minimum_even, index_of_minimum]