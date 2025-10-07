from typing import List

def parse_music(input_sequence: str) -> List[int]:
    mapping: dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}

    def extract_notes(index: int, arr: List[str], acc: List[int]) -> List[int]:
        if index >= len(arr):
            return acc
        element = arr[index]
        return extract_notes(index + 1, arr, acc + [mapping[element]] if element != "" else acc)

    return extract_notes(0, input_sequence.split(" "), [])