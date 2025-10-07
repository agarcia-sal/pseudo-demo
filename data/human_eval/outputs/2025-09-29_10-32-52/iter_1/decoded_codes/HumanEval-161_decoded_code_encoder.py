from typing import List

def solve(string_input: str) -> str:
    flag: int = 0
    index: int = 0
    new_string_list: List[str] = list(string_input)
    for character in string_input:
        if character.isalpha():
            new_string_list[index] = character.swapcase()
            flag = 1
        index += 1
    string_result: str = ''.join(new_string_list)
    if flag == 0:
        return string_result[::-1]
    return string_result