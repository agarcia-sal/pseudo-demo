from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    map_notes: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    # The following loop is a no-op placeholder per pseudocode
    for _ in range(len(music_string)):
        pass

    raw_elements: List[str] = []
    index_var: int = 0
    length: int = len(music_string)
    while index_var < length:
        temp_str: str = ""
        while index_var < length and music_string[index_var] != ' ':
            temp_str += music_string[index_var]
            index_var += 1
        if temp_str:
            raw_elements.append(temp_str)
        index_var += 1

    results: List[int] = [map_notes[element_var] for element_var in raw_elements]

    return results