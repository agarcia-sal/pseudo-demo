from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    durations_map: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    result_list: List[int] = []
    parts_list: List[str] = music_string.split(' ')

    index: int = 0
    while index < len(parts_list):
        current_note: str = parts_list[index]
        if current_note != '':
            result_list.append(durations_map[current_note])
        index += 1

    return result_list