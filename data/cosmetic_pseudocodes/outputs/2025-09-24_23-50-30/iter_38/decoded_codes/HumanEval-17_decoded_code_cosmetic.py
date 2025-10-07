from typing import List, Dict

def parse_music(raw_notes: str) -> List[int]:
    duration_lookup: Dict[str, int] = {'o': 4, '.|': 1, 'o|': 2}
    temp_list: List[int] = []
    for token in raw_notes.split(' '):
        if token != '':
            temp_list.append(duration_lookup[token])
    return temp_list