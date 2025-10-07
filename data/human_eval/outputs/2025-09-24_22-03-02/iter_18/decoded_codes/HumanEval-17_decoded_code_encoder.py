from typing import List

def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    split_list = []
    index = 0
    length_of_music_string = len(music_string)
    while index < length_of_music_string:
        current_char = music_string[index]
        word = ''
        while index < length_of_music_string and current_char != ' ':
            word += current_char
            index += 1
            if index < length_of_music_string:
                current_char = music_string[index]
        if word != '':
            split_list.append(word)
        if index < length_of_music_string and current_char == ' ':
            index += 1
    i = 0
    while i < len(split_list):
        x = split_list[i]
        if x in note_map:
            result.append(note_map[x])
        i += 1
    return result