def add_elements(arr, k):
    total_sum = 0
    index = 0
    while index < k:
        elem = arr[index]
        string_elem = str(elem)
        length_elem = len(string_elem)
        if length_elem <= 2:
            total_sum += elem
        index += 1
    return total_sum