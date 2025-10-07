from typing import List

def string_sequence(n: int) -> str:
    list_of_strings: List[str] = []
    for x in range(n + 1):
        list_of_strings.append(str(x))
    result: str = " ".join(list_of_strings)
    return result