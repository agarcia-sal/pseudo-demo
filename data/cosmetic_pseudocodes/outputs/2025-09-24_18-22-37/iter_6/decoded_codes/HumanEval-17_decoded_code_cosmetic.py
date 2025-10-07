from typing import List

def parse_music(tune_sequence: str) -> List[int]:
    duration_lookup = {'o': 4, 'o|': 2, '.|': 1}
    results_list: List[int] = []
    split_notes = tune_sequence.split(' ')
    index_counter = 0
    while index_counter < len(split_notes):
        if split_notes[index_counter] == '':
            index_counter += 1
            continue
        current_symbol = split_notes[index_counter]
        resolved_value = duration_lookup[current_symbol]
        results_list.append(resolved_value)
        index_counter += 1
    return results_list