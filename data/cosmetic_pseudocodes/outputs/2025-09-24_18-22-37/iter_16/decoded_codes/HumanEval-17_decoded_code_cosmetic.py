from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    temp_map: Dict[str, int] = {
        'o|': 2,
        'o': 4,
        '.|': 1,
    }
    notes: List[str] = music_string.split(' ')
    results: List[int] = []
    idx: int = 0
    while idx < len(notes):
        token = notes[idx]
        if token != '':
            results.append(temp_map[token])
        idx += 1
    return results