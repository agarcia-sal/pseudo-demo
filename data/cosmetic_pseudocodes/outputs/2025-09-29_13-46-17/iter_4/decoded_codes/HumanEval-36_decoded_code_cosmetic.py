from typing import List


def fizz_buzz(integer_n: int) -> int:
    def traverse_and_filter(counter_p: int, accumulator_M: List[int]) -> List[int]:
        if counter_p >= integer_n:
            return accumulator_M
        elif not ((counter_p % 11 != 0) and (counter_p % 13 != 0)):
            return traverse_and_filter(counter_p + 1, accumulator_M + [counter_p])
        else:
            return traverse_and_filter(counter_p + 1, accumulator_M)

    def build_concatenation(list_Q: List[int], idx_v: int, result_S: str) -> str:
        if idx_v >= len(list_Q):
            return result_S
        else:
            return build_concatenation(list_Q, idx_v + 1, result_S + str(list_Q[idx_v]))

    def count_digit_seven(string_X: str, index_i: int, total_O: int) -> int:
        if index_i < 0:
            return total_O
        else:
            is_seven = 1 if string_X[index_i] == '7' else 0
            return count_digit_seven(string_X, index_i - 1, total_O + is_seven)

    filtered_numbers = traverse_and_filter(0, [])
    merged_str = build_concatenation(filtered_numbers, 0, "")
    return count_digit_seven(merged_str, len(merged_str) - 1, 0)