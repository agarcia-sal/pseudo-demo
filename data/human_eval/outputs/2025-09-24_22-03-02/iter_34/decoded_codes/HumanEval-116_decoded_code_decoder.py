def sort_array(arr):
    sorted_arr = sorted(arr)
    for i in range(len(sorted_arr) - 1):
        for j in range(len(sorted_arr) - 1 - i):
            binary_substring = bin(sorted_arr[j])[2:-1]
            count_ones_j = binary_substring.count('1')
            binary_substring_next = bin(sorted_arr[j + 1])[2:-1]
            count_ones_j_plus_1 = binary_substring_next.count('1')
            if count_ones_j > count_ones_j_plus_1:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr