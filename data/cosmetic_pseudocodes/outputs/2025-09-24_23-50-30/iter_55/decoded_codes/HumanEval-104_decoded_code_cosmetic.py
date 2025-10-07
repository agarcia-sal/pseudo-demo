from typing import List


def unique_digits(input_list: List[int]) -> List[int]:
    def contains_only_odd_digits(number: int, digit_str: str) -> bool:
        if not digit_str:
            return True
        head_char = digit_str[0]
        tail_str = digit_str[1:]
        head_digit = int(head_char)
        return (head_digit % 2 == 1) and contains_only_odd_digits(number, tail_str)

    def filter_odds(accumulator: List[int], remaining_list: List[int]) -> List[int]:
        if not remaining_list:
            return accumulator
        current_num = remaining_list[0]
        rest_nums = remaining_list[1:]
        if contains_only_odd_digits(current_num, str(current_num)):
            return filter_odds(accumulator + [current_num], rest_nums)
        else:
            return filter_odds(accumulator, rest_nums)

    filtered_list = filter_odds([], input_list)

    def ascending_order(xs: List[int]) -> List[int]:
        if not xs:
            return []
        min_val = xs[0]
        for element in xs:
            if element < min_val:
                min_val = element
        without_min = xs.copy()
        without_min.remove(min_val)
        return [min_val] + ascending_order(without_min)

    return ascending_order(filtered_list)