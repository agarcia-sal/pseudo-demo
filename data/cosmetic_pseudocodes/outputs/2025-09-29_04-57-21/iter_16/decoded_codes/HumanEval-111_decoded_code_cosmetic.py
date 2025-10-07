from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    characters = test_string.split(" ")
    top_frequency = 0

    position = 0
    while position < len(characters):
        current_char = characters[position]
        if current_char != "":
            freq = characters.count(current_char)
            if freq > top_frequency:
                top_frequency = freq
        position += 1

    if top_frequency > 0:
        index = 0
        while index < len(characters):
            entry = characters[index]
            if characters.count(entry) == top_frequency:
                frequency_map[entry] = top_frequency
            index += 1

    return frequency_map