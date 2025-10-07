from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_lookup: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    for token in music_string.split(" "):
        if len(token) > 0:
            duration_value = duration_lookup[token]
            result_list.append(duration_value)
    return result_list