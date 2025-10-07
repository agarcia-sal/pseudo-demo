from typing import List

def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}
    return [durations[token] for token in music_string.split(' ') if token]