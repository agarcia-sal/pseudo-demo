from typing import List

def parse_music(input_sequence: str) -> List[int]:
    temp_dict: dict[str, int] = {
        'o|': 2,
        '.|': 1,
        'o': 4
    }
    output_list: List[int] = []
    elements_list: List[str] = input_sequence.split(" ")

    idx: int = 0
    while idx < len(elements_list):
        current_element = elements_list[idx]
        if current_element != "":
            output_list.append(temp_dict[current_element])
        idx += 1

    return output_list