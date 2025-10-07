def parse_music(music_string):
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = music_string.split(' ')
    beats_list = []
    for note in notes_list:
        if note != '':
            beats_list.append(note_map[note])
    return beats_list