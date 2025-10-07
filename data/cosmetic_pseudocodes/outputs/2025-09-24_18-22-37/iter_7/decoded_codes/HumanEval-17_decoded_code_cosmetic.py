from typing import List

def parse_music(music_string: str) -> List[int]:
    durations_map: dict[str, int] = {
        'o|': 2,
        'o': 4,
        '.|': 1,
    }
    tokens: List[str] = music_string.split(" ")
    result_list: List[int] = []
    index_counter: int = 0

    while index_counter < len(tokens):
        current_note: str = tokens[index_counter]
        if current_note != "":
            duration_value: int = durations_map[current_note]
            result_list.append(duration_value)
        index_counter += 1

    return result_list