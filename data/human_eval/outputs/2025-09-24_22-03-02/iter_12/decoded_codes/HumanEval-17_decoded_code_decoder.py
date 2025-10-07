from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    note_list = []
    for x in music_string.split(' '):
        if x:
            note_list.append(note_map[x])
    return note_list