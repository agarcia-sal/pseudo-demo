from typing import List

def match_parens(paired_strings: List[str]) -> str:
    def verify_balance(candidate_string: str) -> bool:
        accumulator: int = 0

        def iterate_over(index: int) -> int:
            nonlocal accumulator
            if index == len(candidate_string):
                return accumulator
            current_char = candidate_string[index]
            new_accumulator = accumulator + (1 if current_char == '(' else -1)
            if new_accumulator < 0:
                return -1
            accumulator = new_accumulator
            return iterate_over(index + 1)

        final_value = iterate_over(0)
        return final_value == 0

    merged_first_second = paired_strings[0] + paired_strings[1]
    merged_second_first = paired_strings[1] + paired_strings[0]

    if verify_balance(merged_first_second) or verify_balance(merged_second_first):
        return 'Yes'
    return 'No'