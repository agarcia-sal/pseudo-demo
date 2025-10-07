from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    length_lookup: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    results: List[int] = []
    tokens = music_string.split(" ")

    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token != '':
            results.append(length_lookup[token])
        index += 1

    return results