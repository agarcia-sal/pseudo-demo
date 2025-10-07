from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    tally_map: Dict[str, int] = {}
    tokens = test_string.split(" ")
    peak_count = 0

    for index in range(len(tokens)):
        current_token = tokens[index]
        if current_token != "":
            token_frequency = 0
            for checker in range(len(tokens)):
                if tokens[checker] == current_token:
                    token_frequency += 1
            if token_frequency > peak_count:
                peak_count = token_frequency

    if peak_count <= 0:
        return tally_map

    for index in range(len(tokens)):
        current_token = tokens[index]
        token_frequency = 0
        for checker in range(len(tokens)):
            if tokens[checker] == current_token:
                token_frequency += 1
        if token_frequency == peak_count:
            if current_token not in tally_map:
                tally_map[current_token] = peak_count

    return tally_map