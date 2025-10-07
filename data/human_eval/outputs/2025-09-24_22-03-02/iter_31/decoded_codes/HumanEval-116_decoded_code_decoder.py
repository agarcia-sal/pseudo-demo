def sort_array(arr):
    sorted_by_value = sorted(arr)
    length = len(sorted_by_value)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            count_ones_min = bin(sorted_by_value[min_index]).count('1')
            count_ones_j = bin(sorted_by_value[j]).count('1')
            if count_ones_j < count_ones_min:
                min_index = j
        if min_index != i:
            sorted_by_value[i], sorted_by_value[min_index] = sorted_by_value[min_index], sorted_by_value[i]
    return sorted_by_value