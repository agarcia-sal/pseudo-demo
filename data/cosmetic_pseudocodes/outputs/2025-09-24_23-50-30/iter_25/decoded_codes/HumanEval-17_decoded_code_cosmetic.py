from typing import List

def parse_music(music_string: str) -> List[int]:
    value_map: dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    tokens: List[str] = music_string.split(' ')
    result: List[int] = [value_map[element] for element in tokens if element != '']
    return result