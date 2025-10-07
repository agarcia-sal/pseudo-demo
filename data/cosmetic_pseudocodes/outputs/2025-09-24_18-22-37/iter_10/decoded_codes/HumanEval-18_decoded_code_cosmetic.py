from typing import Literal

def how_many_times(original_string: str, target_substring: str) -> int:
    accumulator: int = 0
    pointer: int = 0
    max_position: int = len(original_string) - len(target_substring)
    while pointer <= max_position:
        # Extract segment equal in length to target_substring
        segment = ''.join(original_string[pointer + offset] for offset in range(len(target_substring)))
        if segment == target_substring:
            accumulator += 1
        pointer += 1
    return accumulator