from typing import List

def parse_music(music_string: str) -> List[int]:
    map_notes: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    results: List[int] = []
    idx: int = 0
    tokens: List[str] = music_string.split(' ')
    while idx < len(tokens):
        current_token: str = tokens[idx]
        idx += 1
        if current_token == '':
            continue
        results.append(map_notes[current_token])
    return results