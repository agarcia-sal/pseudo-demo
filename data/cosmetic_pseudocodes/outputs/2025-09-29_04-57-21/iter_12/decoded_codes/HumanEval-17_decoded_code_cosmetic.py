from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    durations: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    result_list: List[int] = []
    tokens = music_string.split(' ')
    index = 0
    while index < len(tokens):
        current_note = tokens[index]
        if current_note == '':
            index += 1
            continue
        result_list.append(durations[current_note])
        index += 1
    return result_list