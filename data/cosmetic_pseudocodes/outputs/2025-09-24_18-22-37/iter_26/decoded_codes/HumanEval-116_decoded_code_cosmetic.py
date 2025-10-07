from typing import List


def sort_array(numbers_list: List[int]) -> List[int]:
    ascending_ordered: List[int] = []
    idx: int = 0

    while idx < len(numbers_list):
        ascending_ordered.append(numbers_list[idx])
        idx += 1

    ascending_ordered.sort()

    output_list: List[int] = []
    temp_idx: int = 0

    while temp_idx < len(ascending_ordered):
        output_list.append(ascending_ordered[temp_idx])
        temp_idx += 1

    def bit_count_key(value: int) -> int:
        binary_representation: str = bin(value)[2:]  # strip '0b' prefix
        bit_sum: int = 0
        # Count '1's starting from index 3 (0-based) if exists
        for pos in range(3, len(binary_representation)):
            if binary_representation[pos] == '1':
                bit_sum += 1
        return bit_sum

    n: int = len(output_list)
    i: int = 0

    while i < n:
        j: int = i + 1
        while j < n:
            i_key = bit_count_key(output_list[i])
            j_key = bit_count_key(output_list[j])
            if (i_key > j_key) or (i_key == j_key and output_list[i] > output_list[j]):
                output_list[i], output_list[j] = output_list[j], output_list[i]
            j += 1
        i += 1

    return output_list