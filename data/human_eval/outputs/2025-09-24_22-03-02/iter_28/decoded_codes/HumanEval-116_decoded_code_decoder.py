def sort_array(arr):
    sorted_arr = sorted(arr)
    length_arr = len(arr)
    indexed_list = []
    for i in range(length_arr):
        x = sorted_arr[i]
        binary_string = bin(x)
        binary_substring = binary_string[2:]
        count_ones = 0
        length_binary_substring = len(binary_substring)
        for j in range(length_binary_substring):
            if binary_substring[j] == "1":
                count_ones += 1
        indexed_list.append((count_ones, x))
    length_indexed_list = len(indexed_list)
    for i in range(length_indexed_list - 1):
        for k in range(length_indexed_list - 1 - i):
            first_item = indexed_list[k]
            second_item = indexed_list[k + 1]
            if first_item[0] > second_item[0]:
                temp = indexed_list[k]
                indexed_list[k] = indexed_list[k + 1]
                indexed_list[k + 1] = temp
            elif first_item[0] == second_item[0]:
                if first_item[1] > second_item[1]:
                    temp = indexed_list[k]
                    indexed_list[k] = indexed_list[k + 1]
                    indexed_list[k + 1] = temp
    result_list = []
    for i in range(length_indexed_list):
        current_tuple = indexed_list[i]
        result_list.append(current_tuple[1])
    return result_list