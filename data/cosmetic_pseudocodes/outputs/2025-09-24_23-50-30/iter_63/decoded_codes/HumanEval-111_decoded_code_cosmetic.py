from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    occurrences_map: Dict[str, int] = {}
    characters_sequence = input_text.split(" ")
    highest_frequency_value = -1

    for current_char in characters_sequence:
        if current_char != "":
            occurrence_count = characters_sequence.count(current_char)
            if highest_frequency_value < occurrence_count:
                highest_frequency_value = occurrence_count

    if highest_frequency_value > 0:
        for element in characters_sequence:
            if characters_sequence.count(element) == highest_frequency_value:
                occurrences_map[element] = highest_frequency_value

    return occurrences_map