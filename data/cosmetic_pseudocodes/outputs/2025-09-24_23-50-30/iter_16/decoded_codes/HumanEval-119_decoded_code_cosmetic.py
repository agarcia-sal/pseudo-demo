from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def recursive_validate(index_accumulator: List[int]) -> bool:
            index, accumulator = index_accumulator
            if index >= len(string_to_verify):
                return accumulator == 0
            symbol = string_to_verify[index]
            updated_accumulator = accumulator + 1 if symbol == '(' else accumulator - 1
            if updated_accumulator < 0:
                return False
            return recursive_validate([index + 1, updated_accumulator])

        return recursive_validate([0, 0])

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    for condition_result in (check(first_concat), check(second_concat)):
        if condition_result:
            return 'Yes'
    return 'No'