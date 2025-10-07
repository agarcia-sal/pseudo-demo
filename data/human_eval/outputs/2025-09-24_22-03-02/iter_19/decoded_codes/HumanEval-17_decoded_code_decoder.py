from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    result_list: List[int] = []
    split_list: List[str] = []
    index = 0
    length = len(music_string)
    while index < length:
        current_char = music_string[index:index+1]
        if current_char == ' ':
            index += 1
            continue
        temp_str = ''
        while index < length and music_string[index:index+1] != ' ':
            temp_str += music_string[index:index+1]
            index += 1
        split_list.append(temp_str)
    i = 0
    while i < len(split_list):
        x = split_list[i]
        if x in note_map:
            result_list.append(note_map[x])
        i += 1
    return result_list