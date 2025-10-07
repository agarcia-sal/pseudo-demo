from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        tally: int = 0
        for symbol in string_to_verify:
            if symbol == '(':
                tally += 1
            else:
                tally -= 1
            if tally < 0:
                return False
        return tally == 0

    first_concat: str = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat: str = list_of_two_strings[1] + list_of_two_strings[0]
    if check(first_concat) or check(second_concat):
        return "Yes"
    return "No"