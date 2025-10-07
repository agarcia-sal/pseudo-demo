def parse_music(music_string: str) -> list[int]:
    note_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    note_tokens = music_string.split(' ')
    beats_list = []
    for note in note_tokens:
        if note:
            beats_list.append(note_map[note])
    return beats_list