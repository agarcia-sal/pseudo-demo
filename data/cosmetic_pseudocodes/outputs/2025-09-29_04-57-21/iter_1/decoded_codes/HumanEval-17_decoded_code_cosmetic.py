from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    durations: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result: List[int] = [durations[token] for token in music_string.split(' ') if token]
    return result