from typing import List

def parse_music(music_string: str) -> List[int]:
    map_notes = {
        'o|': 2,
        '.|': 1,
        'o': 4,
    }
    tokens_list = music_string.split(' ')
    results: List[int] = []
    for token in tokens_list:
        if token != '':
            results.append(map_notes[token])
    return results