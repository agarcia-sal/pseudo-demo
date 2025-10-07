def sort_array(arr):
    sorted_by_value = sorted(arr)
    def count_ones(x):
        binary_string = bin(x)[2:]
        count_ones = 0
        index = 0
        binary_length = len(binary_string)
        while index < binary_length:
            if binary_string[index] == '1':
                count_ones += 1
            index += 1
        return count_ones
    result = sorted(sorted_by_value, key=count_ones)
    return result