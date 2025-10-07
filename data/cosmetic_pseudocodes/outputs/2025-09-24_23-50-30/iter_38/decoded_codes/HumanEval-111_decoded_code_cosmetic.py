from collections import Counter
from typing import Dict

def histogram(alpha_sequence: str) -> Dict[str, int]:
    fragment_array = alpha_sequence.split(" ")
    counts = Counter(fragment_array)
    peak_frequency = 0

    for symbol in fragment_array:
        if symbol != "":
            count = counts[symbol]
            if count > peak_frequency:
                peak_frequency = count

    tally_map: Dict[str, int] = {}
    if peak_frequency > 0:
        for symbol in fragment_array:
            if counts[symbol] == peak_frequency:
                tally_map[symbol] = peak_frequency

    return tally_map