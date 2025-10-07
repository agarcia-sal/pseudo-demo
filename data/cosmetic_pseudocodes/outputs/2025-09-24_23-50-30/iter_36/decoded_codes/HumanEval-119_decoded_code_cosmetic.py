from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def recur_check(index: int, count: int) -> bool:
            if index >= len(string_to_verify):
                return count == 0
            if count < 0:
                return False
            char = string_to_verify[index]
            count2 = count + 1 if char == '(' else count - 1
            return recur_check(index + 1, count2)
        return recur_check(0, 0)

    first_concat = list_of_two_strings[0] + list_of_two_strings[1]
    second_concat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(first_concat) or check(second_concat):
        return 'Yes'
    return 'No'