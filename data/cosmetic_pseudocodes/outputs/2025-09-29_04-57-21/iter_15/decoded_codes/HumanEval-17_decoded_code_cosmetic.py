from typing import List

def parse_music(music_string: str) -> List[int]:
    duration_lookup = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    token_queue = music_string.split(' ')
    index_counter = 0

    while index_counter < len(token_queue):
        current_token = token_queue[index_counter]
        if current_token != '':
            result_list.append(duration_lookup[current_token])
        index_counter += 1

    return result_list