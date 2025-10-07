def add_elements(arr, k):
    total = 0
    for index in range(k):
        elem = arr[index]
        elem_str = str(elem)
        if len(elem_str) <= 2:
            total += elem
    return total