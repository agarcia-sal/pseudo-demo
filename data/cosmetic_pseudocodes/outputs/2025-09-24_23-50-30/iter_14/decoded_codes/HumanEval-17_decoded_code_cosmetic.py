from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    result: List[int] = []
    index = 0
    tokens = music_string.split(' ')
    while index < len(tokens):
        current_token = tokens[index]
        if current_token.strip() == '':
            index += 1
            continue
        result.append(note_map[current_token])
        index += 1
    return result