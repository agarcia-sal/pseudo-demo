from typing import List

def parse_music(music_string: str) -> List[int]:
    tempo_dict: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    idx: int = 0
    tokens: List[str] = []
    split_chars: set[str] = {' '}
    str_length: int = len(music_string)

    while idx < str_length:
        current_segment = ""
        while idx < str_length and music_string[idx] not in split_chars:
            current_segment += music_string[idx]
            idx += 1
        if current_segment:
            tokens.append(current_segment)
        idx += 1  # skip the split char or move forward

    output_list: List[int] = [tempo_dict[element] for element in tokens if element in tempo_dict]

    return output_list