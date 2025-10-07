from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    note_strings: List[str] = music_string.split(' ')
    durations: List[int] = []
    for note_string in note_strings:
        if note_string and note_string in note_map:
            durations.append(note_map[note_string])
    return durations