from typing import List

def parse_music(music_string: str) -> List[int]:
    result_array: List[int] = []
    duration_lookup = {'o': 4, 'o|': 2, '.|': 1}

    tokens: List[str] = []
    temp_string: str = ''
    for character in music_string + ' ':
        if character != ' ':
            temp_string += character
        elif temp_string:
            tokens.append(temp_string)
            temp_string = ''

    index: int = 0
    while index < len(tokens):
        current_token: str = tokens[index]
        if current_token in duration_lookup:
            result_array.append(duration_lookup[current_token])
        index += 1

    return result_array