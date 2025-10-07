from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    list_of_notes = music_string.split(' ')
    beats_list = []
    for note in list_of_notes:
        if note:
            beats_list.append(note_map[note])
    return beats_list