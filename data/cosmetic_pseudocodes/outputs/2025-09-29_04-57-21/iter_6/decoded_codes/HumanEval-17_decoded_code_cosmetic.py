from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_lookup: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    durations: List[int] = []
    symbols: List[str] = music_string.split(' ')
    for symbol in symbols:
        if symbol:
            durations.append(duration_lookup[symbol])
    return durations