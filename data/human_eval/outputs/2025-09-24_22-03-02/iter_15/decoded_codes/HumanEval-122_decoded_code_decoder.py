def add_elements(arr, k):
    sum_result = 0
    for elem in arr[0:k]:
        elem_string = str(elem)
        if len(elem_string) <= 2:
            sum_result += elem
    return sum_result