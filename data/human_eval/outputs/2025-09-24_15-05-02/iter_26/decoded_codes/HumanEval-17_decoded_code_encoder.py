from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    # Split music_string by spaces and map valid notes to their values
    return [note_map[note] for note in music_string.split(' ') if note]