from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    notes_list: list[str] = music_string.split()
    result: list[int] = []
    for note in notes_list:
        if note:
            if note not in note_map:
                raise ValueError(f"Invalid note '{note}' in music string")
            result.append(note_map[note])
    return result