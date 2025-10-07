from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    split_notes: List[str] = [note for note in music_string.split(' ') if note]
    beat_list: List[int] = [note_map[note] for note in split_notes if note in note_map]
    return beat_list