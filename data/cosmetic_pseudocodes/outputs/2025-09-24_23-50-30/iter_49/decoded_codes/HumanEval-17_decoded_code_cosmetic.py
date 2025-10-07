from typing import List, Dict

def parse_music(input_sequence: str) -> List[int]:
    lookup: Dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    tokens: List[str] = input_sequence.split(' ')

    def unfold(collection: List[str], index: int, accumulator: List[int]) -> List[int]:
        if index >= len(collection):
            return accumulator
        element = collection[index]
        if len(element) != 0:
            return unfold(collection, index + 1, accumulator + [lookup[element]])
        else:
            return unfold(collection, index + 1, accumulator)

    return unfold(tokens, 0, [])