from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        accumulator = 0
        for current_char in string_to_verify:
            if current_char == '(':
                accumulator += 1
            else:
                accumulator -= 1
            if accumulator < 0:
                return False
        return accumulator == 0

    concatA = list_of_two_strings[0]
    concatB = list_of_two_strings[1]
    combined_first = concatA + concatB
    combined_second = concatB + concatA

    if check(combined_first) or check(combined_second):
        return 'Yes'
    else:
        return 'No'