from typing import List, Dict


def parse_music(input_string: str) -> List[int]:
    temp_map: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    result_list: List[int] = []
    split_notes: List[str] = input_string.split(" ")
    index_counter: int = 0
    while index_counter < len(split_notes):
        current_note: str = split_notes[index_counter]
        if current_note != "":
            result_list.append(temp_map[current_note])
        index_counter += 1
    return result_list