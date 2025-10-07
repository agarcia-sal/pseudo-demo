from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    mapping_notes: Dict[str, int] = {
        'o|': 2,
        '.|': 1,
        'o': 4,
    }

    result_notes: List[int] = []
    for token in music_string.split(' '):
        if token == '':
            continue
        result_notes.append(mapping_notes[token])

    return result_notes