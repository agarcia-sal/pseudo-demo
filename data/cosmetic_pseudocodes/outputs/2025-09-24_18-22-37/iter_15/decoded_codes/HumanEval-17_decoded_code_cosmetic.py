from typing import List, Dict


def parse_music(rhythm_code: str) -> List[int]:
    length_by_note_map: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    result_list: List[int] = []
    tokens: List[str] = rhythm_code.split(" ")

    index_var: int = 0
    while index_var < len(tokens):
        current_token: str = tokens[index_var]

        if current_token != "":
            mapped_value: int = length_by_note_map[current_token]
            result_list.append(mapped_value)

        index_var += 1

    return result_list