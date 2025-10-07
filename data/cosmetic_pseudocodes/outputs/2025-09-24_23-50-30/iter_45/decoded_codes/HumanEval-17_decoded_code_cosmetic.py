from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_map: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    tokens: List[str] = music_string.split(' ')
    result_list: List[int] = [duration_map[token] for token in tokens if token != '']
    return result_list