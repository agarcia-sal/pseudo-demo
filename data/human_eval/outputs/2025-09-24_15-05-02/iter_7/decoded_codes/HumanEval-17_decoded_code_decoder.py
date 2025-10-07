from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = []
    for note_symbol in music_string.split(' '):
        if note_symbol:
            notes_list.append(note_map[note_symbol])
    return notes_list