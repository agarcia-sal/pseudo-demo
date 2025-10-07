from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    split_notes = music_string.split(' ')
    result = []
    index = 0
    while index < len(split_notes):
        current_note = split_notes[index]
        if current_note != '':
            note_value = note_map[current_note]
            result.append(note_value)
        index += 1
    return result