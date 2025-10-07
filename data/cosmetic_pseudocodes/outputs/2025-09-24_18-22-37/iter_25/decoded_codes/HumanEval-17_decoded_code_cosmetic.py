from typing import List

def parse_music(music_string: str) -> List[int]:
    temp_dict: dict[str, int] = {"o|": 2, "o": 4, ".|": 1}
    split_notes: List[str] = music_string.split(" ")
    result_list: List[int] = []
    idx: int = 0

    while idx < len(split_notes):
        cur_note = split_notes[idx]
        if cur_note != "":
            val = temp_dict[cur_note]  # key guaranteed to exist by pseudocode assumption
            result_list.append(val)
        idx += 1

    return result_list