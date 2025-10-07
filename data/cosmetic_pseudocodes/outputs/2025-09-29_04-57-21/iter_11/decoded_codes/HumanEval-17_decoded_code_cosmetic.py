from typing import List

def parse_music(music_string: str) -> List[int]:
    duration_for_notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = music_string.split(" ")
    durations: List[int] = []
    idx = 0
    while idx < len(notes_list):
        current_note = notes_list[idx]
        if current_note != "":
            durations.append(duration_for_notes[current_note])
        idx += 1
    return durations