from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    split_notes = music_string.split(' ')
    for current_note in split_notes:
        if current_note != '':
            note_value = note_map[current_note]
            result.append(note_value)
    return result