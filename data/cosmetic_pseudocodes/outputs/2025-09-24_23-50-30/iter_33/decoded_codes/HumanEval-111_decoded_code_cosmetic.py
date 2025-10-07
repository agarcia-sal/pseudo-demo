from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    cache_map: Dict[str, int] = {}
    tokens = input_text.split(' ')
    peak_frequency = 0

    for item in tokens:
        if item != '':
            current_count = sum(1 for element in tokens if element == item)
            if current_count > peak_frequency:
                peak_frequency = current_count

    if peak_frequency > 0:
        for element in tokens:
            count_in_tokens = sum(1 for val in tokens if val == element)
            if count_in_tokens == peak_frequency:
                cache_map[element] = peak_frequency

    return cache_map