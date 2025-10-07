from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequencies: Dict[str, int] = {}
    components = test_string.split(" ")
    top_frequency = 0

    for current_element in components:
        occurrence_count = components.count(current_element)
        if not (occurrence_count <= top_frequency or current_element == ""):
            top_frequency = occurrence_count

    if top_frequency > 0:
        for current_element in components:
            occurrence_count = components.count(current_element)
            if occurrence_count == top_frequency:
                frequencies[current_element] = top_frequency

    return frequencies