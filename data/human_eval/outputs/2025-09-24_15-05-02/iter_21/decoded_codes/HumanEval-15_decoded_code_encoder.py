from typing import List

def string_sequence(n: int) -> str:
    list_of_strings: List[str] = []
    for number in range(n + 1):
        list_of_strings.append(str(number))
    result_string: str = " ".join(list_of_strings)
    return result_string