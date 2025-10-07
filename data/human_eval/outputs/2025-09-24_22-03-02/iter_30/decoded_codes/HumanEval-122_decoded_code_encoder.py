def add_elements(arr, k):
    sum_result = 0
    for index in range(k):
        elem = arr[index]
        elem_string = str(elem)
        length = len(elem_string)
        if length <= 2:
            sum_result += elem
    return sum_result