from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_lookup: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    split_notes: List[str] = music_string.split(" ")
    result_notes: List[int] = []

    for temp_note in split_notes:
        if temp_note != "":
            temp_duration: int = duration_lookup[temp_note]
            result_notes.append(temp_duration)

    return result_notes