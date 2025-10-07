from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    mapping: Dict[str, int] = {'o|': 2, 'o': 4, '.|': 1}
    tokens: List[str] = music_string.split(' ')
    results: List[int] = []
    index: int = len(tokens) - 1

    while index >= 0:
        current: str = tokens[index]
        if current == '':
            index -= 1
            continue
        results.insert(0, mapping[current])
        index -= 1

    return results