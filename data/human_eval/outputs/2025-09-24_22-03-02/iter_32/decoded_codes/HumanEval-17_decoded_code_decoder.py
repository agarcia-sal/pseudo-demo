from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    tokens = music_string.split(' ')
    result = []
    for x in tokens:
        if x != '':
            result.append(note_map[x])
    return result