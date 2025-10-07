from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    split_notes = []
    index = 0
    length = len(music_string)
    while index < length:
        current_char = music_string[index]
        temp_string = ''
        while index < length and current_char != ' ':
            temp_string += current_char
            index += 1
            if index < length:
                current_char = music_string[index]
        split_notes.append(temp_string)
        index += 1
    result = []
    for note in split_notes:
        if note != '':
            result.append(note_map[note])
    return result