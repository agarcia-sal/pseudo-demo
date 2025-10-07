from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_map: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    music_list: List[str] = music_string.split(" ")
    idx: int = 0
    while idx < len(music_list):
        if music_list[idx] != "":
            result_list.append(duration_map[music_list[idx]])
        idx += 1
    return result_list