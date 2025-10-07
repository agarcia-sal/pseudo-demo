from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    note_map: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    tokens = music_string.split(' ')
    beats_list: List[int] = []
    for token in tokens:
        if token:
            beats_list.append(note_map[token])
    return beats_list