def add_elements(arr, k):
    sum_result = 0
    for index in range(k):
        elem = arr[index]
        elem_str = str(elem)
        length = 0
        for _ in elem_str:
            length += 1
        if length <= 2:
            sum_result += elem
    return sum_result