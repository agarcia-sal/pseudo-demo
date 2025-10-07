from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    duration_lookup: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    tokens: List[str] = music_string.split(' ')
    durations: List[int] = []

    idx: int = 0
    while idx < len(tokens):
        token = tokens[idx]
        if token != '':
            durations.append(duration_lookup[token])
        idx += 1

    return durations