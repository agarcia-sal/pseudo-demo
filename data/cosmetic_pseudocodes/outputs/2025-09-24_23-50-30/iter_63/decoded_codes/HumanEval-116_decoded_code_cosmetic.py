from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones_in_binary(n: int) -> int:
        bit_str = ""
        quotient = n
        while quotient > 0:
            bit_str = str(quotient % 2) + bit_str
            quotient //= 2
        ones_count = 0
        for digit in bit_str:
            ones_count += 1 if digit == "1" else 0
        return ones_count

    temp_sorted = array_of_integers[:]
    n = len(temp_sorted)
    for i in range(1, n):
        for j in range(n - i):
            if temp_sorted[j] > temp_sorted[j + 1]:
                tmp_var = temp_sorted[j]
                temp_sorted[j] = temp_sorted[j + 1]
                temp_sorted[j + 1] = tmp_var

    def recursive_key_sort(input_list: List[int]) -> List[int]:
        if not input_list:
            return []
        pivot = input_list[0]
        less_partition: List[int] = []
        equal_partition: List[int] = []
        greater_partition: List[int] = []
        pivot_ones = count_ones_in_binary(pivot)
        for item in input_list:
            item_ones = count_ones_in_binary(item)
            if item_ones > pivot_ones:
                greater_partition.append(item)
            elif item_ones == pivot_ones:
                equal_partition.append(item)
            else:
                less_partition.append(item)
        return recursive_key_sort(less_partition) + equal_partition + recursive_key_sort(greater_partition)

    return recursive_key_sort(temp_sorted)