from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    note_duration_map: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = music_string.split(' ')
    result: List[int] = []
    index = 0
    while index < len(notes_list):
        if notes_list[index] != '':
            result.append(note_duration_map[notes_list[index]])
        index += 1
    return result