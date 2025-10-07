from typing import List

def parse_music(music_string: str) -> List[int]:
    def get_value(key: str) -> int:
        if key == 'o':
            return 4
        if key == 'o|':
            return 2
        if key == '.|':
            return 1
        return 0  # default for unrecognized keys

    output_list: List[int] = []
    keys_list: List[str] = []
    idx_counter: int = 0
    str_len: int = len(music_string)

    while idx_counter < str_len:
        temp_note = ""
        # Collect characters until space or end of string
        while idx_counter < str_len and music_string[idx_counter] != " ":
            temp_note += music_string[idx_counter]
            idx_counter += 1
        if temp_note:
            keys_list.append(temp_note)
        idx_counter += 1  # skip space

    for elem in keys_list:
        output_list.append(get_value(elem))

    return output_list