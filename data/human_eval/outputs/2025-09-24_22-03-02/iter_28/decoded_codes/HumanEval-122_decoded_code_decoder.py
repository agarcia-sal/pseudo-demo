def add_elements(arr, k):
    sum_result = 0
    for index in range(0, k):
        elem = arr[index]
        elem_str = str(elem)
        elem_length = len(elem_str)
        if elem_length <= 2:
            sum_result += elem
    return sum_result