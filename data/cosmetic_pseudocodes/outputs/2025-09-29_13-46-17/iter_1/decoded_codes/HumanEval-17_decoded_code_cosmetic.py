from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    note_duration_map: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    durations: List[int] = [note_duration_map[element] for element in music_string.split(' ') if element]
    return durations