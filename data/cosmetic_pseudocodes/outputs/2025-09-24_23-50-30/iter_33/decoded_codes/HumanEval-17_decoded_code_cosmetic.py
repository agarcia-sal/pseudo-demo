from typing import List

def parse_music(input_string: str) -> List[int]:
    duration_lookup = {'o': 4, 'o|': 2, '.|': 1}
    parts_list = input_string.split(' ')
    idx = 0
    results: List[int] = []
    while idx < len(parts_list):
        if parts_list[idx] != '':
            results.append(duration_lookup[parts_list[idx]])
        idx += 1
    return results