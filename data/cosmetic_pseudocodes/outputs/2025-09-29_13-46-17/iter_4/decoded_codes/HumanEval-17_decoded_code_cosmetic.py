from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    note_duration_map: Dict[str, int] = {'o|': 2, '.|': 1, 'o': 4}

    def convert_notes(notes_list: List[str], index: int, accumulator: List[int]) -> List[int]:
        if index == len(notes_list):
            return accumulator
        current_note = notes_list[index]
        updated_accumulator = accumulator + [note_duration_map[current_note]] if current_note != "" else accumulator
        return convert_notes(notes_list, index + 1, updated_accumulator)

    split_notes = music_string.split(" ")
    return convert_notes(split_notes, 0, [])