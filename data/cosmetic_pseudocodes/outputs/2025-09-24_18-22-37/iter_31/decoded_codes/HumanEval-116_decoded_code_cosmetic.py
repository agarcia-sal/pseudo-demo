from typing import List, Tuple


def sort_array(input_list: List[int]) -> List[int]:
    temp_sorted_list: List[int] = input_list.copy()
    temp_sorted_list.sort()  # sort in place ascending

    helper_list: List[Tuple[int, int]] = []

    for item in temp_sorted_list:
        binary_str = bin(item)[2:]  # binary representation without '0b'
        ones_counter = 0
        # Count '1's in bits starting from index 1 to end + 1 (1-based index == 3 to length+2 zero-based)
        # Corresponds to binary_str[1:] since 3 - 2 = 1 and length(binary_str) + 2 - 2 = len(binary_str)
        for index in range(3, len(binary_str) + 3):  # since range end is exclusive, +3 needed
            if binary_str[index - 2] == '1':  # index-2 to adjust zero-based indexing
                ones_counter += 1
        helper_list.append((item, ones_counter))

    # Bubble sort helper_list by the second element (ones_counter)
    n = len(helper_list)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if helper_list[i][1] > helper_list[j][1]:
                helper_list[i], helper_list[j] = helper_list[j], helper_list[i]

    sorted_result: List[int] = [pair[0] for pair in helper_list]
    return sorted_result