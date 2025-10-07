from typing import List

def parse_music(music_string: str) -> List[int]:
    length_lookup: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    results: List[int] = []
    for each_token in music_string.split(' '):
        if len(each_token) > 0:
            results.append(length_lookup[each_token])
    return results