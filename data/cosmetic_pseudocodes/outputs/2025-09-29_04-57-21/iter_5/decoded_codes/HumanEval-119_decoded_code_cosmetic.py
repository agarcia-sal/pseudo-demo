from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(target_str: str) -> bool:
        accumulator: int = 0

        def recursive_iter(index: int) -> bool:
            nonlocal accumulator
            if index >= len(target_str):
                return accumulator == 0

            if target_str[index] != ')':
                accumulator += 1
            else:
                accumulator -= 1

            if accumulator < 0:
                return False
            return recursive_iter(index + 1)

        return recursive_iter(0)

    combined_a: str = list_of_two_strings[0] + list_of_two_strings[1]
    combined_b: str = list_of_two_strings[1] + list_of_two_strings[0]

    if check(combined_a) or check(combined_b):
        return "Yes"
    return "No"