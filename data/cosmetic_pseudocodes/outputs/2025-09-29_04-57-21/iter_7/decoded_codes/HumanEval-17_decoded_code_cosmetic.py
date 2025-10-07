from typing import List

def parse_music(music_string: str) -> List[int]:
    duration_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result: List[int] = []
    tokens: List[str] = music_string.split(' ')
    idx: int = 0
    while idx < len(tokens):
        if tokens[idx] != '':
            result.append(duration_map[tokens[idx]])
        idx += 1
    return result