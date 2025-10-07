from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    tokens = test_string.split(' ')
    tally_map: Dict[str, int] = {}
    peak_frequency: int = -1

    def scan_for_peak(index: int) -> None:
        nonlocal peak_frequency
        if index >= len(tokens):
            return
        current_token = tokens[index]
        current_count = sum(1 for element in tokens if element != "" and element == current_token)
        if current_count > peak_frequency:
            peak_frequency = current_count
        scan_for_peak(index + 1)

    scan_for_peak(0)

    if peak_frequency > 0:
        position = 0
        while position < len(tokens):
            candidate = tokens[position]
            candidate_count = sum(1 for element in tokens if element != "" and element == candidate)
            if candidate_count == peak_frequency:
                tally_map[candidate] = peak_frequency
            position += 1

    return tally_map