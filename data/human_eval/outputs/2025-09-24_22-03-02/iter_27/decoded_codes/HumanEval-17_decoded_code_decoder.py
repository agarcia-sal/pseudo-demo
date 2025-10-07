from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    split_list = []
    i = 0
    length = len(music_string)
    while i < length:
        current_char = music_string[i]
        if current_char == ' ':
            i += 1
            continue
        token = ''
        while i < length and music_string[i] != ' ':
            token += music_string[i]
            i += 1
        split_list.append(token)
    result_list = []
    j = 0
    while j < len(split_list):
        x = split_list[j]
        if x != '':
            value = note_map[x]
            result_list.append(value)
        j += 1
    return result_list