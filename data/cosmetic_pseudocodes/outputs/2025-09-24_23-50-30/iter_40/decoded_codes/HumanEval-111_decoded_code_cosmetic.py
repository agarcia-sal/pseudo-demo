from typing import Dict

def histogram(alpha_string: str) -> Dict[str, int]:
    tokens_list = alpha_string.split(" ")
    peak_frequency = 0

    for element in tokens_list:
        current_freq = tokens_list.count(element)
        if current_freq > peak_frequency and element != "":
            peak_frequency = current_freq

    tally_map: Dict[str, int] = {}
    if peak_frequency > 0:
        for item in tokens_list:
            if tokens_list.count(item) == peak_frequency:
                tally_map[item] = peak_frequency

    return tally_map