from typing import List

def parse_music(music_string: str) -> List[int]:
    duration_lookup: dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    tokens_list = music_string.split(' ')
    output_sequence: List[int] = []

    for current_token in tokens_list:
        if current_token != '':
            output_sequence.append(duration_lookup[current_token])
    return output_sequence