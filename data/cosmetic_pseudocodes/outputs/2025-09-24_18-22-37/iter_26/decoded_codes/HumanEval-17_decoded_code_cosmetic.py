from typing import List

def parse_music(music_string: str) -> List[int]:
    duration_lookup: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    result_list: List[int] = []
    pieces: List[str] = music_string.split(' ')
    idx: int = 0
    while idx < len(pieces):
        current_piece: str = pieces[idx]
        if current_piece == '':
            idx += 1
            continue
        tmp_val: int = duration_lookup[current_piece]
        result_list.append(tmp_val)
        idx += 1
    return result_list