from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    mapping: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    tokens_list: List[str] = [token for token in music_string.split(' ') if len(token) > 0]
    result_list: List[int] = [mapping[token] for token in tokens_list]
    return result_list