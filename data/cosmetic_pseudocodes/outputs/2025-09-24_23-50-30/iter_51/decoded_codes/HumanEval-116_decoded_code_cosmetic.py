from typing import List


def sort_array(sequence_of_numbers: List[int]) -> List[int]:
    def calc_ones(binary_string: str, index: int, tally: int) -> int:
        if index == len(binary_string):
            return tally
        return calc_ones(binary_string, index + 1, tally + (1 if binary_string[index] == "1" else 0))

    def key_function(n: int) -> int:
        # bin(n) gives '0b...' so skip first 3 chars to start at 4th char (index 3)
        return calc_ones(bin(n)[3:], 1, 0)

    def recursive_sort(input_list: List[int], accumulator: List[int]) -> List[int]:
        if not input_list:
            return accumulator
        min_element = input_list[0]
        rest = input_list[1:]
        less: List[int] = []
        equal: List[int] = [min_element]
        greater: List[int] = []
        for item in rest:
            if item < min_element:
                less.append(item)
            elif item == min_element:
                equal.append(item)
            else:
                greater.append(item)
        return recursive_sort(less, accumulator) + equal + recursive_sort(greater, [])

    temp_sorted = recursive_sort(sequence_of_numbers, [])
    final_sorted = recursive_sort(temp_sorted, [])
    return final_sorted