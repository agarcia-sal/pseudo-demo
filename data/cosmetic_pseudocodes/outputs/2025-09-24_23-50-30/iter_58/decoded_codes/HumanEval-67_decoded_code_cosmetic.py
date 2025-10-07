from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def parse_digits_rec(cur_lst: List[int], cur_elements: List[str]) -> List[int]:
        if not cur_elements:
            return cur_lst
        cur_element, *remaining_elements = cur_elements
        if cur_element.isdigit():
            return parse_digits_rec(cur_lst + [int(cur_element)], remaining_elements)
        return parse_digits_rec(cur_lst, remaining_elements)

    acc_numbers = parse_digits_rec([], string_description.split())

    def sum_iter(nums: List[int]) -> int:
        idx = 0
        total = 0
        while idx < len(nums):
            total += nums[idx]
            idx += 1
        return total

    return total_number_of_fruits - sum_iter(acc_numbers)