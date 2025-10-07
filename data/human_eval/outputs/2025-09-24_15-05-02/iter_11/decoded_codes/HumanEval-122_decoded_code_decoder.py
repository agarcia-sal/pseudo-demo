def add_elements(array, k):
    total_sum = 0
    for element in array[:k]:
        if len(str(element)) <= 2:
            total_sum += element
    return total_sum