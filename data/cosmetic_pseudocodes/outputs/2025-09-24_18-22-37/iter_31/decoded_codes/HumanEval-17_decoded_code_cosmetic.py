from typing import List, Dict

def parse_music(input_sequence: str) -> List[int]:
    duration_lookup: Dict[str, int] = {
        'o|': 2,
        'o': 4,
        '.|': 1,
    }
    split_notes: List[str] = input_sequence.split(" ")
    parsed_notes: List[int] = []
    index_counter: int = 0
    while index_counter < len(split_notes):
        symbol: str = split_notes[index_counter]
        if symbol != "":
            parsed_notes.append(duration_lookup[symbol])
        index_counter += 1
    return parsed_notes