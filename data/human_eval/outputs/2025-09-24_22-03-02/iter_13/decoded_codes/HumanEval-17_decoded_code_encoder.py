def parse_music(music_string) -> list[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    split_list = music_string.split(' ')
    result_list = []
    for x in split_list:
        if x != '':
            result_list.append(note_map[x])
    return result_list