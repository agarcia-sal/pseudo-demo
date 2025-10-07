from typing import Dict

def histogram(alpha_sequence: str) -> Dict[str, int]:
    tally_map: Dict[str, int] = {}
    tokens = alpha_sequence.split(" ")
    top_frequency: int = 0
    position: int = 0

    while position < len(tokens):
        current_token: str = tokens[position]
        if current_token != "":
            current_count: int = 0
            checker: int = 0
            while checker < len(tokens):
                if tokens[checker] == current_token:
                    current_count += 1
                checker += 1
            if current_count > top_frequency:
                top_frequency = current_count
        position += 1

    if top_frequency > 0:
        indexer: int = 0
        while indexer < len(tokens):
            test_token: str = tokens[indexer]
            if test_token != "":
                counted: int = 0
                inner_pos: int = 0
                while inner_pos < len(tokens):
                    if tokens[inner_pos] == test_token:
                        counted += 1
                    inner_pos += 1
                if counted == top_frequency and test_token not in tally_map:
                    tally_map[test_token] = top_frequency
            indexer += 1

    return tally_map