def parse_music(music_string):
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    tokens = music_string.split()
    beats_list = []
    for token in tokens:
        if token:
            beats_list.append(note_map[token])
    return beats_list