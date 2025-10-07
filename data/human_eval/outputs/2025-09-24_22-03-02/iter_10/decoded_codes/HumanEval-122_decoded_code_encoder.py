def add_elements(arr, k):
    total = 0
    for elem in arr[:k]:
        if len(str(elem)) <= 2:
            total += elem
    return total