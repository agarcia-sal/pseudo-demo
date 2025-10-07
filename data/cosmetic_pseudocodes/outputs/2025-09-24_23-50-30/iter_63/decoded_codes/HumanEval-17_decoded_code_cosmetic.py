from typing import List

def parse_music(music_string: str) -> List[int]:
    duration_dict: dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    segments: List[int] = [
        duration_dict[token] for token in music_string.split(' ') if len(token) > 0
    ]
    return segments