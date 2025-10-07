from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def verify_at(index: int, depth: int) -> bool:
            if index == len(string_to_verify):
                return depth == 0
            ch = string_to_verify[index]
            if depth < 0:  # early rejection if depth negative
                return False
            if ch == '(':
                return verify_at(index + 1, depth + 1)
            else:
                return verify_at(index + 1, depth - 1)

        return verify_at(0, 0)

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat) or check(second_concat):
        return 'Yes'
    return 'No'