from typing import List


def string_sequence(integer_n: int) -> str:
    lists_of_strings: List[str] = []
    counter: int = 0
    while counter <= integer_n:
        lists_of_strings.append(str(counter))
        counter += 1
    assembled: str = ""
    index: int = 0
    length: int = len(lists_of_strings)
    while index < length:
        assembled += lists_of_strings[index]
        if index < length - 1:
            assembled += " "
        index += 1
    return assembled