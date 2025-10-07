from typing import List

def parse_music(music_string: str) -> List[int]:
    durations_by_note: dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    tokens: List[str] = music_string.split(" ")
    result_list: List[int] = []
    for index in range(len(tokens)):
        current_token = tokens[index]
        if current_token != "":
            result_list.append(durations_by_note[current_token])
    return result_list