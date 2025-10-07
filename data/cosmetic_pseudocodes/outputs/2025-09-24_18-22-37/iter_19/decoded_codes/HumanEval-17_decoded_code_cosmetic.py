from typing import List

def parse_music(music_string: str) -> List[int]:
    helper_map: dict[str, int] = {'o|': 0x2, 'o': 4, '.|': 0x1}
    split_notes: List[str] = music_string.split(' ')
    durations: List[int] = []
    idx: int = 0

    while idx < len(split_notes):
        current_note = split_notes[idx]
        if current_note != '':
            mapped_value = helper_map[current_note]
            durations.append(mapped_value)
        idx += 1

    return durations