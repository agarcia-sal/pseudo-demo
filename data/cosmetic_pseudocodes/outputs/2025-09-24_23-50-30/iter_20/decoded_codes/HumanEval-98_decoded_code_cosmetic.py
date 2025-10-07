from typing import List

def count_upper(string_input: str) -> int:
    total: int = 0
    positions: List[int] = []
    ptr: int = 0
    while ptr <= len(string_input) - 1:
        positions.append(ptr)
        ptr += 2
    # Filter positions where character is a vowel uppercase letter among A, E, I, O, U
    filtered_positions = [
        pos for pos in positions
        if not (
            string_input[pos] <= 'A'
            or string_input[pos] >= 'Z'
            or (
                string_input[pos] != 'A'
                and string_input[pos] != 'E'
                and string_input[pos] != 'I'
                and string_input[pos] != 'O'
                and string_input[pos] != 'U'
            )
        )
    ]
    total = len(filtered_positions)
    return total