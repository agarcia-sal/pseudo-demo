from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result: List[int] = []
    for x in music_string.split(' '):
        if x:
            if x not in note_map:
                raise ValueError(f"Invalid note symbol: {x}")
            result.append(note_map[x])
    return result