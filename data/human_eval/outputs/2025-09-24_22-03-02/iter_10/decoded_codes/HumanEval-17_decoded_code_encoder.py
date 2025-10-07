def parse_music(music_string):
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    for x in music_string.split(' '):
        if x:
            result.append(note_map[x])
    return result