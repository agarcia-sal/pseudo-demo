from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    split_list = music_string.split(' ')
    result_list = []
    index = 0
    while index < len(split_list):
        element = split_list[index]
        if element != '':
            value = note_map[element]
            result_list.append(value)
        index += 1
    return result_list