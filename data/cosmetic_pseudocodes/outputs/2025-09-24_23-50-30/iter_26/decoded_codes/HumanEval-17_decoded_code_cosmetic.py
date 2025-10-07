from typing import List

def parse_music(music_string: str) -> List[int]:
    index_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    tokens: List[str] = [token for token in music_string.split(" ") if len(token) > 0]
    return [index_map[token] for token in tokens]