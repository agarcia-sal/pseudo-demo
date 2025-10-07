from typing import List, Dict

def parse_music(music_string: str) -> List[int]:
    note_collection = List[str]
    sequence_stack: List[str] = []
    index_counter: int = 0
    duration_map: Dict[str, int] = {}
    result_stack: List[int] = []

    duration_map = {'o|': 2, 'o': 4, '.|': 1}

    def parse_stack(sc: note_collection, idx: int, acc: List[int]) -> List[int]:
        if idx >= len(sc):
            return acc
        current_note: str = sc[idx]
        value_to_add: int = 0
        if current_note != '':
            value_to_add = duration_map.get(current_note, 0)
        if value_to_add > 0:
            acc = acc + [value_to_add]
        return parse_stack(sc, idx + 1, acc)

    sequence_stack = music_string.split(' ')
    return parse_stack(sequence_stack, 0, result_stack)