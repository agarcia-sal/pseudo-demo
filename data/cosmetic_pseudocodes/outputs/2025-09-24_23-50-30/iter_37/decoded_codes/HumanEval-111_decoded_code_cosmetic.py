from typing import Dict

def histogram(alpha: str) -> Dict[str, int]:
    tally: Dict[str, int] = {}
    symbols = alpha.split(" ")
    top_frequency = -1

    # Find the highest frequency of any non-empty symbol
    for index in range(len(symbols)):
        current = symbols[index]
        count_current = 0
        for item in symbols:
            if item == current:
                count_current += 1
        if current != "" and count_current > top_frequency:
            top_frequency = count_current

    # Collect all symbols that have this top frequency
    if top_frequency > 0:
        for i in range(len(symbols)):
            candidate = symbols[i]
            freq_candidate = 0
            for elem in symbols:
                if elem == candidate:
                    freq_candidate += 1
            if freq_candidate == top_frequency:
                tally[candidate] = top_frequency

    return tally