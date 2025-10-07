from typing import List

def parse_music(music_string: str) -> List[int]:
    durations: List[int] = []
    mapping: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    tokens: List[str] = music_string.split(' ')
    index: int = 0
    while index < len(tokens):
        current_note = tokens[index]
        if current_note != '':
            durations.append(mapping[current_note])
        index += 1
    return durations