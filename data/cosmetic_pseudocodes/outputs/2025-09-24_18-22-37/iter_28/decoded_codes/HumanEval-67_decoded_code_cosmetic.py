from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    container: List[int] = []
    iterator: int = 0

    while iterator < len(string_description):
        delimiter_positions: List[int] = [i for i, ch in enumerate(string_description) if ch == ' ']
        current_word: str = ""

        if len(delimiter_positions) > 0:
            current_word = string_description[:delimiter_positions[0]]
            string_description = string_description[delimiter_positions[0] + 1 :]
        else:
            current_word = string_description
            string_description = ""

        status_flag: bool = False
        character_index: int = 0

        while character_index < len(current_word):
            char_value = current_word[character_index]
            if '0' <= char_value <= '9':
                status_flag = True
            else:
                status_flag = False
                break
            character_index += 1

        if status_flag:
            container.append(int(current_word))

        iterator += 1
        if string_description == "":
            break

    accumulator: int = 0
    index_variable: int = 0
    while index_variable < len(container):
        accumulator += container[index_variable]
        index_variable += 1

    return total_number_of_fruits + (~accumulator + 1)