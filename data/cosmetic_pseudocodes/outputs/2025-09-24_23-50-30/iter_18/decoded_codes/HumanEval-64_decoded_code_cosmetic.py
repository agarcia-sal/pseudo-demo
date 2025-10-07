from typing import Dict


def vowels_count(string_input: str) -> int:
    vowels_map: Dict[str, bool] = {char: True for char in "aeiouAEIOU"}

    count_accumulator = 0
    index_counter = 0
    input_length = len(string_input)

    while index_counter < input_length:
        if vowels_map.get(string_input[index_counter], False):
            count_accumulator += 1
        index_counter += 1

    if input_length == 0:
        return count_accumulator  # handle empty string without indexing

    last_character = string_input[input_length - 1]
    if last_character != 'y' and last_character != 'Y':
        return count_accumulator

    return count_accumulator + 1