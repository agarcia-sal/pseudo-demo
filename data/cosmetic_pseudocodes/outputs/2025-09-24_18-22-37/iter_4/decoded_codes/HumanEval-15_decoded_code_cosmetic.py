from typing import List

def string_sequence(integer_n: int) -> str:
    index: int = 0
    string_list: List[str] = []
    while index <= integer_n:
        string_list.append(str(index))
        index += 1

    result_string: str = ""
    pos: int = 1
    while pos <= len(string_list):
        if pos == len(string_list):
            result_string += string_list[pos - 1]
        else:
            result_string += string_list[pos - 1] + " "
        pos += 1

    return result_string