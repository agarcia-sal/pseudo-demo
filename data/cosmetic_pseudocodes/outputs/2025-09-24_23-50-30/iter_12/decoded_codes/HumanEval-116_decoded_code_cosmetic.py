from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones(binary_string: str) -> int:
        return sum(1 for char in binary_string if char == '1')

    temp_list: List[int] = []
    index: int = 0
    while index < len(array_of_integers):
        item = array_of_integers[index]
        temp_list = temp_list + [item]
        index += 1

    temp_list = sorted(temp_list)

    def sort_by_ones(list_to_sort: List[int]) -> List[int]:
        if len(list_to_sort) <= 1:
            return list_to_sort
        else:
            pivot = list_to_sort[0]
            # bin() returns strings like '0b...' so skip first two chars
            pivot_key = count_ones(bin(pivot)[2:])
            less_equal: List[int] = []
            greater: List[int] = []

            for i in range(1, len(list_to_sort)):
                current = list_to_sort[i]
                current_key = count_ones(bin(current)[2:])
                if current_key <= pivot_key:
                    less_equal = less_equal + [current]
                else:
                    greater = greater + [current]

            left_sorted = sort_by_ones(less_equal)
            right_sorted = sort_by_ones(greater)

            return left_sorted + [pivot] + right_sorted

    return sort_by_ones(temp_list)