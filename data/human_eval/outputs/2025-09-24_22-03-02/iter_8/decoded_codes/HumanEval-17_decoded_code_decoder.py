from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {
        "o": 4,
        "o|": 2,
        ".|": 1
    }
    note_list: List[int] = []
    for note in music_string.split():
        if note:
            note_list.append(note_map[note])
    return note_list