from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    tokens = music_string.split(' ')
    result: List[int] = []
    for index in range(len(tokens)):
        x = tokens[index]
        if x != '':
            result.append(note_map[x])
    return result