from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    result_list = []
    split_list = music_string.split(' ')
    for x in split_list:
        if x != '':
            value = note_map.get(x)
            result_list.append(value)
    return result_list