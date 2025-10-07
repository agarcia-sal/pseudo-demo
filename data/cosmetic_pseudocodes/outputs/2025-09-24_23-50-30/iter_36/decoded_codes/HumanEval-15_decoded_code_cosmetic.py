from typing import List

def string_sequence(integer_n: int) -> str:
    temp_array: List[str] = []
    iterator: int = 0

    while iterator <= integer_n:
        temp_array.append(str(iterator))
        iterator += 1

    result_string: str = ""
    index: int = 0
    length: int = len(temp_array)

    if length == 0:
        return result_string

    result_string = temp_array[0]

    while index + 1 < length:
        index += 1
        result_string += " " + temp_array[index]

    return result_string