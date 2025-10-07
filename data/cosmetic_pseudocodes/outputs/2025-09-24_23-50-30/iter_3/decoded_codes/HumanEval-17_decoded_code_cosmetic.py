from typing import List

def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    elements = music_string.split(" ")
    # Loop from index 1 to end, skipping index 0
    for idx in range(1, len(elements)):
        element = elements[idx]
        if len(element) > 0:
            result_list.append(durations[element])
    return result_list