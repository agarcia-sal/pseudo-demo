from typing import List

def parse_music(music_string: str) -> List[int]:
    temp_dict: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    tokens = music_string.split(' ')
    for token in tokens:
        if token:
            result_list.append(temp_dict[token])
    return result_list