def add_elements(arr, k):
    total = 0
    index = 0
    while index < k:
        elem = arr[index]
        elem_string = str(elem)
        length = 0
        char_index = 0
        while char_index < len(elem_string):
            length += 1
            char_index += 1
        if length <= 2:
            total += elem
        index += 1
    return total