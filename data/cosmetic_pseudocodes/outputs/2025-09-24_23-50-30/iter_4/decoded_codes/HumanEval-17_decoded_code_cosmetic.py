from typing import List

def parse_music(music_string: str) -> List[int]:
    note_duration_map: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}

    def extract_notes(index: int, notes_list: List[int], tokens: List[str]) -> List[int]:
        if index >= len(tokens):
            return notes_list
        elif tokens[index] != "":
            return extract_notes(index + 1, notes_list + [note_duration_map[tokens[index]]], tokens)
        else:
            return extract_notes(index + 1, notes_list, tokens)

    return extract_notes(0, [], music_string.split(" "))