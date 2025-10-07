from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        counter: int = 0
        idx: int = 0
        length: int = len(string_to_verify)
        while idx < length:
            current_char: str = string_to_verify[idx]
            if current_char == '(':
                counter += 1
            else:
                counter -= 1

            if counter < 0:
                return False
            idx += 1

        return counter == 0

    first_concat: str = list_of_two_strings[0]
    second_part: str = list_of_two_strings[1]
    first_combined: str = first_concat + second_part

    second_concat: str = list_of_two_strings[1]
    first_part: str = list_of_two_strings[0]
    second_combined: str = second_concat + first_part

    if check(first_combined):
        return 'Yes'
    if check(second_combined):
        return 'Yes'
    return 'No'