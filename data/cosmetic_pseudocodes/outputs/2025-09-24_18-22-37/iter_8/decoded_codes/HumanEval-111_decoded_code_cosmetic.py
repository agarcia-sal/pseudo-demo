from typing import Dict

def histogram(input_sequence: str) -> Dict[str, int]:
    tally_map: Dict[str, int] = {}
    characters_list = input_sequence.split(" ")
    top_frequency = 0

    iterator_index = 0
    length_chars = len(characters_list)
    while iterator_index < length_chars:
        current_char = characters_list[iterator_index]
        char_count = characters_list.count(current_char)

        if current_char != "":
            if char_count > top_frequency:
                top_frequency = char_count
        iterator_index += 1

    if top_frequency > 0:
        for index in range(length_chars):
            examined_char = characters_list[index]
            examined_char_count = characters_list.count(examined_char)
            if examined_char_count == top_frequency:
                tally_map[examined_char] = top_frequency

    return tally_map