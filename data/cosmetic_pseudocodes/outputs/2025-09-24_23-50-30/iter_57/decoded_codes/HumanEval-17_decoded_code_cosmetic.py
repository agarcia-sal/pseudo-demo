from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    mapping_local: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    tokens_local: List[str] = music_string.split(' ')
    result_local: List[int] = []

    index_local: int = 0
    while index_local < len(tokens_local):
        token_local: str = tokens_local[index_local]
        if token_local != '':
            result_local.append(mapping_local[token_local])
        index_local += 1

    return result_local