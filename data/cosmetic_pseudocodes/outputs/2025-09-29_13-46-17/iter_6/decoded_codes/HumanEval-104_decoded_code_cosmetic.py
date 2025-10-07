from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def contains_only_odd_digits(number_xyz: int) -> bool:
        s = str(number_xyz)

        def check_digit(index_abc: int) -> bool:
            if index_abc == len(s):
                return True
            digit_num = int(s[index_abc])
            if digit_num % 2 == 0:
                return False
            return check_digit(index_abc + 1)

        return check_digit(0)

    def quicksort_ascending(arr_list: List[int]) -> List[int]:
        if not arr_list:
            return []
        head = arr_list[0]
        tail = arr_list[1:]
        less_equal = [v for v in tail if v <= head]
        greater = [v for v in tail if v > head]
        return quicksort_ascending(less_equal) + [head] + quicksort_ascending(greater)

    accumulator_505: List[int] = []

    def process_elements(idx_counter: int) -> None:
        if idx_counter == len(list_of_positive_integers):
            return
        current_val_34 = list_of_positive_integers[idx_counter]
        if contains_only_odd_digits(current_val_34):
            accumulator_505.append(current_val_34)
        process_elements(idx_counter + 1)

    process_elements(0)
    return quicksort_ascending(accumulator_505)