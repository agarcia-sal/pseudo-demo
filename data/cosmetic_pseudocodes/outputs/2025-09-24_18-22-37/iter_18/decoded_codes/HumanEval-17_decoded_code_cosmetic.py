from typing import List, Dict


def parse_music(symbol_sequence: str) -> List[int]:
    duration_by_note: Dict[str, int] = {
        'o': 0x4,
        'o|': 2,
        '.|': 1,
    }
    tokens: List[str] = symbol_sequence.split(' ')
    output_list: List[int] = []

    index_counter: int = 0
    while index_counter < len(tokens):
        current_token: str = tokens[index_counter]
        if current_token != '':
            duration_value: int = duration_by_note[current_token]
            output_list.append(duration_value)
        index_counter += 1

    return output_list