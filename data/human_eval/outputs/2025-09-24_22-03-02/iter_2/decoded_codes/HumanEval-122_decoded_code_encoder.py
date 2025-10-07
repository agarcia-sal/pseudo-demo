def add_elements(arr, k):
    sum_total = 0
    for elem in arr[:k]:
        if len(str(elem)) <= 2:
            sum_total += elem
    return sum_total