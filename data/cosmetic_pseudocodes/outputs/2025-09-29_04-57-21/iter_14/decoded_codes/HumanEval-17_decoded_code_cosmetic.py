from typing import List

def parse_music(music_string: str) -> List[int]:
    duration_lookup: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    parsed_durations: List[int] = []
    cursor: int = 0
    tokens: List[str] = music_string.split(" ")
    while cursor < len(tokens):
        if tokens[cursor] != "":
            parsed_durations.append(duration_lookup[tokens[cursor]])
        cursor += 1
    return parsed_durations