from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    symbols = test_string.split(" ")
    top_frequency = -1

    # Determine the highest frequency of non-empty symbols
    for ch in symbols:
        if ch != "":
            freq = symbols.count(ch)
            if freq > top_frequency:
                top_frequency = freq

    freq_map: Dict[str, int] = {}
    if top_frequency > 0:
        # Add all symbols with frequency equal to top_frequency to freq_map
        for ch in symbols:
            if ch != "" and symbols.count(ch) == top_frequency:
                freq_map[ch] = top_frequency

    return freq_map