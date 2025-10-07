from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    notes_list: List[int] = []
    split_notes: list[str] = music_string.split(' ')
    for note in split_notes:
        if note:
            if note in note_map:
                notes_list.append(note_map[note])
            else:
                # If the note is not found in the note_map, skip it or raise an error
                # Choosing to skip unknown notes to stay robust
                continue
    return notes_list