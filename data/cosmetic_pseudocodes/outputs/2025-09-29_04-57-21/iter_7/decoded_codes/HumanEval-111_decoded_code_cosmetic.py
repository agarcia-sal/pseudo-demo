from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    tokens_list = test_string.split(' ')
    max_frequency = 0

    idx = 0
    while idx < len(tokens_list):
        current_token = tokens_list[idx]
        current_count = tokens_list.count(current_token)
        if not (current_count <= max_frequency or current_token == ""):
            max_frequency = current_count
        idx += 1

    if max_frequency > 0:
        for element in tokens_list:
            element_count = tokens_list.count(element)
            if element_count == max_frequency:
                frequency_map[element] = max_frequency

    return frequency_map