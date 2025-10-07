from typing import List

def parse_music(input_sequence: str) -> List[int]:
    duration_lookup: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    return [duration_lookup[token] for token in input_sequence.split(" ") if token != ""]