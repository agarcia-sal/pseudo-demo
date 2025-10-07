from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        if integer_value < 0:
            integer_value = -integer_value

        digits_str = str(integer_value)

        def convert_str_to_list_of_ints(string_val: str, idx: int) -> List[int]:
            if idx == len(string_val):
                return []
            return [int(string_val[idx])] + convert_str_to_list_of_ints(string_val, idx + 1)

        list_of_digits = convert_str_to_list_of_ints(digits_str, 0)

        if integer_value == 0:
            return 0

        if array_of_integers[0] < 0:
            list_of_digits[0] = -list_of_digits[0]

        def sum_list(numbers: List[int], idx: int, accumulator: int) -> int:
            if idx == len(numbers):
                return accumulator
            return sum_list(numbers, idx + 1, accumulator + numbers[idx])

        return sum_list(list_of_digits, 0, 0)

    def map_function(funct, lst: List[int], idx: int) -> List[int]:
        if idx == len(lst):
            return []
        return [funct(lst[idx])] + map_function(funct, lst, idx + 1)

    intermediate_results = map_function(digits_sum, array_of_integers, 0)

    def filter_positive(lst: List[int], idx: int, accumulator: List[int]) -> List[int]:
        if idx == len(lst):
            return accumulator
        if lst[idx] > 0:
            accumulator = accumulator + [lst[idx]]
        return filter_positive(lst, idx + 1, accumulator)

    positive_elements = filter_positive(intermediate_results, 0, [])

    def length_of(lst: List[int], idx: int) -> int:
        if idx == len(lst):
            return 0
        return 1 + length_of(lst, idx + 1)

    return length_of(positive_elements, 0)