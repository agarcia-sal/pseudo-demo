def pluck(arr):
    if len(arr) == 0:
        return ['']
    evens = []
    index = 0
    while index < len(arr):
        element = arr[index]
        modulo_result = element % 2
        if modulo_result == 0:
            evens.append(element)
        index += 1
    if len(evens) == 0:
        return ['']
    min_even = evens[0]
    min_index = 0
    index = 1
    while index < len(evens):
        if evens[index] < min_even:
            min_even = evens[index]
        index += 1
    arr_index = 0
    while arr_index < len(arr):
        if arr[arr_index] == min_even:
            min_index = arr_index
            break
        arr_index += 1
    return [min_even, min_index]