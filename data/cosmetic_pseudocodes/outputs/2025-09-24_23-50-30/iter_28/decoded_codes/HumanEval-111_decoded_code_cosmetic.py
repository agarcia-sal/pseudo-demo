from collections import defaultdict
from typing import Dict


def histogram(input_data: str) -> Dict[str, int]:
    tally_map: Dict[str, int] = defaultdict(int)
    tokens = input_data.split(" ")
    peak_frequency = -1

    def get_maximum(index: int) -> int:
        nonlocal peak_frequency
        if index >= len(tokens):
            return peak_frequency
        entry = tokens[index]
        count_entry = 0
        for item in tokens:
            if item == entry:
                count_entry += 1
        if entry != "" and count_entry > peak_frequency:
            peak_frequency = count_entry
        return get_maximum(index + 1)

    peak_frequency = get_maximum(0)

    def populate_map(i: int) -> None:
        if i < len(tokens):
            elt = tokens[i]
            elt_freq = 0
            for x in tokens:
                if x == elt:
                    elt_freq += 1
            if elt_freq == peak_frequency:
                tally_map[elt] = elt_freq
            populate_map(i + 1)

    if peak_frequency > 0:
        populate_map(0)

    return tally_map