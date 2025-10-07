from typing import List

def parse_music(music_string: str) -> List[int]:
    mapping: dict[str, int] = {
        'o|': 2,
        'o': 4,
        '.|': 1,
    }
    result_list: List[int] = []
    tokens_array: List[str] = music_string.split(' ')
    for current_token in tokens_array:
        if not current_token:
            continue
        result_list.append(mapping[current_token])
    return result_list