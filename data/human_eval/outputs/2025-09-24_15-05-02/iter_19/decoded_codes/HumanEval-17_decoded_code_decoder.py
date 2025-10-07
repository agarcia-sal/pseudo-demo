from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    notes_list: List[str] = music_string.split(' ')
    result_list: List[int] = []
    for note in notes_list:
        if note:
            result_list.append(note_map[note])
    return result_list