def sort_array(arr):
    sorted_by_value = sorted(arr)
    def key_func(x):
        binary_representation = bin(x)
        binary_string = binary_representation[2:]
        count_ones = 0
        index = 0
        while index < len(binary_string):
            if binary_string[index] == '1':
                count_ones += 1
            index += 1
        return count_ones
    result = sorted(sorted_by_value, key=key_func)
    return result