from typing import List

def parse_music(string_input: str) -> List[int]:
    map_notes: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    tokens = [token for token in string_input.split(' ') if token]
    results: List[int] = [map_notes[token] for token in tokens]
    return results