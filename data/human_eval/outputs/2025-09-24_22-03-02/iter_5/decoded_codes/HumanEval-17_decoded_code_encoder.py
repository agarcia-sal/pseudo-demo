def parse_music(music_string):
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    list_of_notes = []
    for note in music_string.split(' '):
        if note:
            list_of_notes.append(note_map[note])
    return list_of_notes