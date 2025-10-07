from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    character_list: List[str] = []
    index: int = 0

    while index < len(input_string):
        current_char = input_string[index]
        if current_char == ",":
            character_list.append(" ")
        else:
            character_list.append(current_char)
        index += 1

    concatenated_string = ""
    i = 0
    while True:
        if i == len(character_list):
            break
        concatenated_string += character_list[i]
        i += 1

    return concatenated_string.split(" ")