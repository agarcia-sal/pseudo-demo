from typing import List


def solve(textual_data: str) -> str:
    flag_marker: bool = False
    pointer: int = 0
    characters_array: List[str] = []

    while pointer < len(textual_data):
        current_char = textual_data[pointer]

        if not current_char.isalpha():
            characters_array.append(current_char)
            pointer += 1
            continue

        if 'a' <= current_char <= 'z':
            characters_array.append(current_char.upper())
        else:
            characters_array.append(current_char.lower())

        flag_marker = True
        pointer += 1

    result_string = ""
    position = 0

    while position < len(characters_array):
        result_string += characters_array[position]
        position += 1

    if not flag_marker:
        reversed_result = ""
        back_index = len(result_string) - 1

        while back_index >= 0:
            reversed_result += result_string[back_index]
            back_index -= 1

        return reversed_result

    return result_string