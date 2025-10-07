from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    split_notes = music_string.split(' ')
    result: List[int] = []
    i = 0
    while i < len(split_notes):
        x = split_notes[i]
        if x != '':
            result.append(note_map[x])
        i += 1
    return result