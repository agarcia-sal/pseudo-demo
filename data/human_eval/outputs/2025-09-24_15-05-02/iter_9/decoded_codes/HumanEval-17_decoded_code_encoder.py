def parse_music(music_string):
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[value] for value in music_string.split(' ') if value]