from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    length_for_note: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_collection: List[int] = []
    for token in music_string.split(' '):
        if token != '':
            result_collection.append(length_for_note[token])
    return result_collection