from typing import List

def parse_music(jumble_input: str) -> List[int]:
    note_time: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    parts = jumble_input.split(' ')
    idx = 0
    while idx < len(parts):
        sp = parts[idx]
        idx += 1
        if sp != '':
            number = note_time[sp]
            result_list.append(number)
    return result_list