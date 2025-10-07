def add_elements(arr, k):
    sum_result = 0
    for index in range(k):
        elem = arr[index]
        string_representation = str(elem)
        length_of_string = len(string_representation)
        if length_of_string <= 2:
            sum_result += elem
    return sum_result