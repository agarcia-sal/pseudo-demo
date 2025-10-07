def add_elements(arr, k):
    total = 0
    for index in range(k):
        elem = arr[index]
        elem_str = str(elem)
        length = len(elem_str)
        if length <= 2:
            total += elem
    return total