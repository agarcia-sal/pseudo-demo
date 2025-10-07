from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        accumulator: int = 0
        index_counter: int = 0
        length: int = len(string_to_verify)
        while index_counter < length:
            current_element: str = string_to_verify[index_counter]
            if current_element == '(':
                accumulator += 1
            else:
                accumulator -= 1
            if accumulator < 0:
                return False
            index_counter += 1
        return accumulator == 0

    first_joined: str = list_of_two_strings[0] + list_of_two_strings[1]
    second_joined: str = list_of_two_strings[1] + list_of_two_strings[0]
    if check(first_joined) or check(second_joined):
        return 'Yes'
    return 'No'