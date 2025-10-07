from typing import List

def parse_music(music_string: str) -> List[int]:
    def HelperProcess(notes_array: List[str], index: int, acc: List[int]) -> List[int]:
        if index >= len(notes_array):
            return acc
        mapping_dict = {'o': 4, 'o|': 2, '.|': 1}
        note = notes_array[index]
        if note:
            val = mapping_dict[note]
            return HelperProcess(notes_array, index + 1, acc + [val])
        else:
            return HelperProcess(notes_array, index + 1, acc)

    splitted_notes: List[str] = []
    cur_pos = 0
    start_pos = 0
    while cur_pos < len(music_string):
        if music_string[cur_pos] == ' ':
            if start_pos < cur_pos:
                splitted_notes.append(music_string[start_pos:cur_pos])
            start_pos = cur_pos + 1
        cur_pos += 1
    if start_pos < len(music_string):
        splitted_notes.append(music_string[start_pos:])

    return HelperProcess(splitted_notes, 0, [])