from typing import List

def string_sequence(number_limit: int) -> str:
    list_of_strings: List[str] = []
    for integer in range(number_limit + 1):
        list_of_strings.append(str(integer))
    result_string: str = " ".join(list_of_strings)
    return result_string