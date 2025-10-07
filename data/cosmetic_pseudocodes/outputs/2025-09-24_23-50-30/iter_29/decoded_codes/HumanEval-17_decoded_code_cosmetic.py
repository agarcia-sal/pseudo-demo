from typing import List

def parse_music(music_string: str) -> List[int]:
    x_occurrences: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    p_notes: List[int] = []

    for each_symbol in music_string.split(" "):
        if each_symbol != "":
            p_notes.append(x_occurrences[each_symbol])

    return p_notes