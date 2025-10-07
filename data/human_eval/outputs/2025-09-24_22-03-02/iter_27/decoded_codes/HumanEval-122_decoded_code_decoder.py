def add_elements(arr, k) -> int:
    sum_result = 0
    for index in range(k):
        elem = arr[index]
        elem_str = str(elem)
        length_elem_str = len(elem_str)
        if length_elem_str <= 2:
            sum_result += elem
    return sum_result