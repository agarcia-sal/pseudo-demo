from typing import List


def fizz_buzz(integer_n: int) -> int:
    def extract_multiples(curr_idx: int, limit: int, acc_list: List[int]) -> List[int]:
        if not (curr_idx < limit):
            return acc_list
        # Include curr_idx if divisible by 11 or 13
        if (curr_idx % 11 == 0) or (curr_idx % 13 == 0):
            new_list = acc_list + [curr_idx]
        else:
            new_list = acc_list
        return extract_multiples(curr_idx + 1, limit, new_list)

    def join_numbers(num_list: List[int], acc_str: str) -> str:
        if not num_list:
            return acc_str
        return join_numbers(num_list[1:], acc_str + str(num_list[0]))

    def count_char_7(s: str, idx: int, acc_count: int) -> int:
        if not (idx < len(s)):
            return acc_count
        increment = 1 if s[idx] == '7' else 0
        return count_char_7(s, idx + 1, acc_count + increment)

    multiples_list = extract_multiples(0, integer_n, [])
    merged_string = join_numbers(multiples_list, "")
    return count_char_7(merged_string, 0, 0)