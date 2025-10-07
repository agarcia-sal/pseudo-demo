def add_elements(arr, k):
    sum_result = 0
    for elem in arr[:k]:
        if len(str(elem)) <= 2:
            sum_result += elem
    return sum_result