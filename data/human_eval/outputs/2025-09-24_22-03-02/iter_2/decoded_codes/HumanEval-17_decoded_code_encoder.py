def parse_music(music_string: str) -> list[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    tokens = music_string.split(' ')
    result = []
    for token in tokens:
        if token:
            result.append(note_map[token])
    return result