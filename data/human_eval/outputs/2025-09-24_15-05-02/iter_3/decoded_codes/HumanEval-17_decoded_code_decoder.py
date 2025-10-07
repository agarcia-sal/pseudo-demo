def parse_music(music_string: str) -> list[int]:
    # Map of note representations to their integer values
    note_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string by spaces and map each note to its value if not empty
    result = [note_map[note] for note in music_string.split() if note]

    return result