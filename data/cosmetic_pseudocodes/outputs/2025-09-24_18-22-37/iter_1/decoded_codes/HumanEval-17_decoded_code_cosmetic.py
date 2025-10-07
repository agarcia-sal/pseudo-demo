from typing import List

def parse_music(music_string: str) -> List[int]:
    note_duration_map: dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    durations: List[int] = []
    for note in music_string.split(' '):
        if note:
            durations.append(note_duration_map[note])
    return durations