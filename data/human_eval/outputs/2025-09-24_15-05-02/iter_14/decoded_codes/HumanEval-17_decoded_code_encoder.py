def parse_music(music_string):
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split(' ')
    result = []
    for note in notes:
        if note != '':
            result.append(note_map[note])
    return result