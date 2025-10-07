from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = music_string.split()
    beats_list: List[int] = []
    for note in notes_list:
        if note:
            # Map note to beat count; assume note is guaranteed to be in note_map
            beats_list.append(note_map[note])
    return beats_list