from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    char_frequencies: Dict[str, int] = {}
    characters = test_string.split(" ")
    top_frequency = -1

    idx = 0
    while idx < len(characters):
        current_char = characters[idx]
        if current_char != "":
            occurrence_count = characters.count(current_char)
            if occurrence_count > top_frequency:
                top_frequency = occurrence_count
        idx += 1

    if top_frequency > 0:
        j = 0
        while j < len(characters):
            candidate = characters[j]
            if characters.count(candidate) == top_frequency:
                char_frequencies[candidate] = top_frequency
            j += 1

    return char_frequencies