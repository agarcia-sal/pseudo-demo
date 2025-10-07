from typing import List, Dict


def parse_music(music_string: str) -> List[int]:
    duration_lookup: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    tokens: List[str] = music_string.split(' ')

    def accumulate(index: int) -> None:
        if index >= len(tokens):
            return
        current_token = tokens[index]
        if current_token:
            result_list.append(duration_lookup[current_token])
        accumulate(index + 1)

    accumulate(0)
    return result_list