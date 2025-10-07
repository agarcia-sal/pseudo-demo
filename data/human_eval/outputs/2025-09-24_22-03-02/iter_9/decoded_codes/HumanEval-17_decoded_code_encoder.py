def parse_music(music_string: str) -> list[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    split_notes = music_string.split(' ')
    result_list = []
    for x in split_notes:
        if x != '':
            result_list.append(note_map[x])
    return result_list