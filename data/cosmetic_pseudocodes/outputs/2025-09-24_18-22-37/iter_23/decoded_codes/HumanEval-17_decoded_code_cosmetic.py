from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_lookup: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    split_notes: List[str] = music_string.split(' ')
    result_list: List[int] = []
    idx: int = 0
    while idx < len(split_notes):
        current_note: str = split_notes[idx]
        if current_note != '':
            temp_duration: int = duration_lookup[current_note]
            result_list.append(temp_duration)
        idx += 1
    return result_list