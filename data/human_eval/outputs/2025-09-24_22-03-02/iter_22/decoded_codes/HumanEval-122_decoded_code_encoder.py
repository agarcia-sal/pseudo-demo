def add_elements(arr, k):
    sum_result = 0
    index = 0
    while index < k:
        elem = arr[index]
        elem_str = str(elem)
        length = len(elem_str)
        if length <= 2:
            sum_result += elem
        index += 1
    return sum_result