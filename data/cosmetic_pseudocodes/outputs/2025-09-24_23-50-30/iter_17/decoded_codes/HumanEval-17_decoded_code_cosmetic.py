from typing import List

def parse_music(music_string: str) -> List[int]:
    note_to_time: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    tokens: List[str] = music_string.split(' ')
    result: List[int] = []
    for element in tokens:
        if element == '':
            continue
        result.append(note_to_time[element])
    return result