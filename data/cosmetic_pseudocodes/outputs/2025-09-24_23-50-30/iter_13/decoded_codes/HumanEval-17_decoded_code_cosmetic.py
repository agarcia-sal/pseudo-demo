from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    duration_for_note: Dict[str, int] = {}
    duration_for_note['o'] = 4
    duration_for_note['o|'] = 2
    duration_for_note['.|'] = 1

    tokens_list: List[str] = [s for s in music_string.split(' ') if s != '']
    result_list: List[int] = []

    for token in tokens_list:
        result_list.append(duration_for_note[token])

    return result_list