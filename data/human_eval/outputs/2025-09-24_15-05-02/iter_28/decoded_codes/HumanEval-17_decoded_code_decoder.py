from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    note_map: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    notes_list: List[str] = music_string.split()
    return [note_map[x] for x in notes_list if x]