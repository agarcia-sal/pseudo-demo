def parse_music(music_string):
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    note_tokens = music_string.split(' ')
    beats_list = [note_map[note_token] for note_token in note_tokens if note_token]
    return beats_list