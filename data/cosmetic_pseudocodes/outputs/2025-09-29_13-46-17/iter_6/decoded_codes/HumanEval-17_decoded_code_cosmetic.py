from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    dic_notes: Dict[str, int] = {
        "o|": 2,
        ".|": 1,
        "o": 4,
    }

    music_string_split: List[str] = []
    i__idx: int = 0
    n_music_string: int = len(music_string)
    while i__idx < n_music_string:
        acc = ""
        while i__idx < n_music_string and music_string[i__idx] != " ":
            acc += music_string[i__idx]
            i__idx += 1
        music_string_split.append(acc)
        while i__idx < n_music_string and music_string[i__idx] == " ":
            i__idx += 1

    def helper_result(accumulated_list: List[int], idx: int) -> List[int]:
        if idx >= len(music_string_split):
            return accumulated_list
        _currNote = music_string_split[idx]
        if _currNote != "":
            accumulated_list_next = accumulated_list + [dic_notes[_currNote]]
        else:
            accumulated_list_next = accumulated_list
        return helper_result(accumulated_list_next, idx + 1)

    return helper_result([], 0)