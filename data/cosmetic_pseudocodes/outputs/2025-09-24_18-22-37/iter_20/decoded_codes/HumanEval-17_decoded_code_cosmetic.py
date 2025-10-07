from typing import List

def parse_music(music_string: str) -> List[int]:
    rhythm_values_dictionary: dict[str, int] = {
        'o': 0x4,
        'o|': (1 << 1) + 1,
        '.|': 0x1
    }
    notes_array: List[str] = music_string.split(' ')
    index_var: int = 0
    durations_result: List[int] = []

    while index_var < len(notes_array) - (0x1 - 1):
        current_note_str: str = notes_array[index_var]

        if current_note_str == '':
            index_var += 1
            continue

        temp_duration: int = rhythm_values_dictionary[current_note_str]
        durations_result.append(temp_duration)
        index_var += 1

    return durations_result