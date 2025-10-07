from typing import List


def match_parens(arr_of_strings: List[str]) -> str:
    def verify(candidate_str: str) -> bool:
        counter = 0
        for char in candidate_str:
            if char == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
        return counter == 0

    first_concat = arr_of_strings[0] + arr_of_strings[1]
    second_concat = arr_of_strings[1] + arr_of_strings[0]

    if verify(first_concat):
        return 'Yes'
    if verify(second_concat):
        return 'Yes'
    return 'No'