def add_elements(arr, k):
    total_sum = 0
    for index in range(k):
        elem = arr[index]
        elem_str = str(elem)
        elem_length = len(elem_str)
        if elem_length <= 2:
            total_sum += elem
    return total_sum