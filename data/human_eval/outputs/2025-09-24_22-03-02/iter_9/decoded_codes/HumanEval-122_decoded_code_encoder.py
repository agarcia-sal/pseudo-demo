def add_elements(arr, k):
    total = 0
    for element in arr[:k]:
        if len(str(element)) <= 2:
            total += element
    return total