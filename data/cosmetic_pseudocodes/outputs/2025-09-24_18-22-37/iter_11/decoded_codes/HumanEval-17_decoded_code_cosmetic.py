from typing import List

def parse_music(music_string: str) -> List[int]:
    duration_lookup = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    result_list: List[int] = []
    tokens = music_string.split(' ')
    idx_counter = 0
    while idx_counter < len(tokens):
        current_token = tokens[idx_counter]
        if current_token != '':
            mapped_value = duration_lookup[current_token]
            result_list.append(mapped_value)
        idx_counter += 1

    return result_list