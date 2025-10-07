def parse_music(music_string: str) -> list[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    result_list = []
    split_notes = []
    current_index = 0
    music_length = len(music_string)
    while current_index < music_length:
        current_char = music_string[current_index]
        if current_char == ' ':
            current_index += 1
            continue
        temp_string = ''
        while current_index < music_length and music_string[current_index] != ' ':
            temp_string += music_string[current_index]
            current_index += 1
        split_notes.append(temp_string)
    i = 0
    while i < len(split_notes):
        note = split_notes[i]
        if note in note_map:
            result_list.append(note_map[note])
        i += 1
    return result_list