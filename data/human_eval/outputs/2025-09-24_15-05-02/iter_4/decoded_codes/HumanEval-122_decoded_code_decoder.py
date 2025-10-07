def add_elements(arr, k):
    total_sum = 0
    for element in arr[:k]:
        element_string = str(element)
        if len(element_string) <= 2:
            total_sum += element
    return total_sum