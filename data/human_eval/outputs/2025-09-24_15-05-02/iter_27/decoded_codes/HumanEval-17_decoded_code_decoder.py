from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    notes_list: List[str] = music_string.split()
    beats_list: List[int] = []
    for note in notes_list:
        if note:
            try:
                beats_list.append(note_map[note])
            except KeyError as e:
                raise ValueError(f"Invalid note '{note}' encountered") from e
    return beats_list