from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_lookup: Dict[str, int] = {
        'o|': 2,
        'o': 4,
        '.|': 1
    }

    result_list: List[int] = []
    tokens: List[str] = music_string.split(" ")
    index_counter: int = 0

    while index_counter < len(tokens):
        current_note: str = tokens[index_counter]

        if len(current_note) != 0:
            mapped_duration: int = duration_lookup[current_note]
            result_list.append(mapped_duration)

        index_counter += 1

    return result_list