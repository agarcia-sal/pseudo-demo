def add_elements(arr, k):
    total = 0
    for i in range(k):
        elem = arr[i]
        string_elem = str(elem)
        length_of_string = len(string_elem)
        if length_of_string <= 2:
            total += elem
    return total