from typing import List


def parse_music(music_string: str) -> List[int]:
    noteDurationMap: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    tokens: List[str] = music_string.split(' ')
    results: List[int] = [noteDurationMap[token] for token in tokens if token != '']
    return results