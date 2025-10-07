from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    tmp_list = music_string.split(' ')
    result: List[int] = []
    for each_elem in tmp_list:
        if each_elem != '':
            result.append(note_map[each_elem])
    return result