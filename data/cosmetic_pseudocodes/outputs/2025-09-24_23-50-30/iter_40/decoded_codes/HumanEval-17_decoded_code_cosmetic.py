from typing import List

def parse_music(music_string: str) -> List[int]:
    temp_container: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    return [temp_container[element] for element in music_string.split(' ') if element != '']