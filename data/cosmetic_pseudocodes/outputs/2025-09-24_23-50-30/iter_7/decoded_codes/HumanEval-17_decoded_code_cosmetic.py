from typing import List


def parse_music(input_sequence: str) -> List[int]:
    mapping_dictionary: dict[str, int] = {
        'o|': 2,
        '.|': 1,
        'o': 4
    }

    def helper(tokens: List[str], accumulator: List[int], idx: int) -> List[int]:
        if idx >= len(tokens):
            return accumulator
        if len(tokens[idx]) > 0:
            accumulator.append(mapping_dictionary[tokens[idx]])
        return helper(tokens, accumulator, idx + 1)

    return helper(input_sequence.split(' '), [], 0)