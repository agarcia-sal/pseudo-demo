from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    duration_lookup: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    tokens: List[str] = music_string.split(' ')
    index: int = 0

    while index < len(tokens):
        token = tokens[index]
        if token != '':
            result_list.append(duration_lookup[token])
        index += 1

    return result_list