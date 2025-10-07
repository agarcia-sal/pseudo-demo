from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        net_count = 0

        def iterate_chars(position: int) -> bool:
            nonlocal net_count
            if position >= len(string_to_verify):
                return True

            current_char = string_to_verify[position]
            if current_char != '(':
                net_count -= 1
            else:
                net_count += 1

            if net_count < 0:
                return False

            return iterate_chars(position + 1)

        return iterate_chars(0) and net_count == 0

    merged_first_last = list_of_two_strings[0] + list_of_two_strings[1]
    merged_last_first = list_of_two_strings[1] + list_of_two_strings[0]

    if check(merged_first_last):
        return "Yes"
    if check(merged_last_first):
        return "Yes"
    return "No"