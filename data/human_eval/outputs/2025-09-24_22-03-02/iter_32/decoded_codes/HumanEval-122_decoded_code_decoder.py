def add_elements(arr, k):
    sum_result = 0
    index = 0
    while index < k:
        string_repr = str(arr[index])
        length_of_string = len(string_repr)
        if length_of_string <= 2:
            sum_result += arr[index]
        index += 1
    return sum_result