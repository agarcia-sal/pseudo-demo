from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_dictionary: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    tokens_queue: List[str] = music_string.split(' ')
    idx: int = 0
    while idx < len(tokens_queue):
        token = tokens_queue[idx]
        if token != '':
            result_list.append(duration_dictionary[token])
        idx += 1
    return result_list