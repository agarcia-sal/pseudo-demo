from typing import List


def fizz_buzz(next_value: int) -> int:
    def gather(accumulate_list: List[int], current_val: int) -> List[int]:
        if current_val >= next_value:
            return accumulate_list
        proceed_list = accumulate_list
        if current_val % 13 == 0 or current_val % 11 == 0:
            proceed_list = accumulate_list + [current_val]
        return gather(proceed_list, current_val + 1)

    collected_numbers = gather([], 0)

    def combine_strings(string_list: List[int], index: int, length: int, acc_string: str) -> str:
        if index == length:
            return acc_string
        return combine_strings(string_list, index + 1, length, acc_string + str(string_list[index]))

    joint_string = combine_strings(collected_numbers, 0, len(collected_numbers), "")

    def count_characters(text: str, pos: int, lim: int, accumulator: int) -> int:
        if pos == lim:
            return accumulator
        increment = 1 if text[pos] == '7' else 0
        return count_characters(text, pos + 1, lim, accumulator + increment)

    return count_characters(joint_string, 0, len(joint_string), 0)