from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    local_map: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    token_list = music_string.split()
    for current_token in token_list:
        if current_token:
            result_list.append(local_map[current_token])
    return result_list