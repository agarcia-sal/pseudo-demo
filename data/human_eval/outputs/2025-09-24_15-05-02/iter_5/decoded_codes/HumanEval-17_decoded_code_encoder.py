def parse_music(music_string: str) -> list[int]:
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = []
    for note_string in music_string.split(' '):
        if note_string:
            notes_list.append(note_map[note_string])
    return notes_list