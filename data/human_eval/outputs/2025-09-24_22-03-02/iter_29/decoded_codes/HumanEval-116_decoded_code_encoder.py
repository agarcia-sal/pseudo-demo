def sort_array(arr):
    sorted_by_value = []
    for i in range(len(arr)):
        sorted_by_value.append(arr[i])
    sorted_by_value.sort()
    sorted_by_bits = []
    for i in range(len(sorted_by_value)):
        current_element = sorted_by_value[i]
        count_ones = 0
        binary_representation = bin(current_element)[2:]
        for j in range(len(binary_representation)):
            if binary_representation[j] == '1':
                count_ones += 1
        sorted_by_bits.append((count_ones, current_element))
    for i in range(len(sorted_by_bits) - 1):
        for j in range(len(sorted_by_bits) - 1 - i):
            if sorted_by_bits[j][0] > sorted_by_bits[j + 1][0] or (sorted_by_bits[j][0] == sorted_by_bits[j + 1][0] and sorted_by_bits[j][1] > sorted_by_bits[j + 1][1]):
                temp = sorted_by_bits[j]
                sorted_by_bits[j] = sorted_by_bits[j + 1]
                sorted_by_bits[j + 1] = temp
    result = []
    for i in range(len(sorted_by_bits)):
        result.append(sorted_by_bits[i][1])
    return result