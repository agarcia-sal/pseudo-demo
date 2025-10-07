def binary_representation_of(x: int) -> str:
    if x == 0:
        return '0b0'
    n = x
    bits = []
    while n > 0:
        remainder = n % 2
        bits.insert(0, str(remainder))
        n //= 2
    binary_string = '0b' + ''.join(bits)
    return binary_string

def sort_array(arr):
    sorted_arr = sorted(arr)
    length_arr = len(sorted_arr)
    result = []
    for index in range(length_arr):
        min_index = index
        for j in range(index + 1, length_arr):
            x_binary = binary_representation_of(sorted_arr[min_index])
            count_ones_min = 0
            for k in range(2, len(x_binary)):
                if x_binary[k] == '1':
                    count_ones_min += 1
            y_binary = binary_representation_of(sorted_arr[j])
            count_ones_j = 0
            for k in range(2, len(y_binary)):
                if y_binary[k] == '1':
                    count_ones_j += 1
            if count_ones_j < count_ones_min or (count_ones_j == count_ones_min and sorted_arr[j] < sorted_arr[min_index]):
                min_index = j
        if min_index != index:
            temp = sorted_arr[index]
            item_at_min = sorted_arr[min_index]
            sorted_arr[index] = item_at_min
            sorted_arr[min_index] = temp
    result = sorted_arr
    return result