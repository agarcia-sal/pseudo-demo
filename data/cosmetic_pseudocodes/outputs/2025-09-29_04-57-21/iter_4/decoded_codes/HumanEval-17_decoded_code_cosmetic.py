from typing import List

def parse_music(music_string: str) -> List[int]:
    durations: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    tokens: List[str] = music_string.split(' ')
    index: int = 0

    while index < len(tokens):
        current_token: str = tokens[index]
        if current_token != '':
            result_list.append(durations[current_token])
        index += 1

    return result_list