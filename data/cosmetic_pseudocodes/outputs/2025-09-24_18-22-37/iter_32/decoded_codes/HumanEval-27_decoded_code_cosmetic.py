from typing import Sequence

def flip_case(alpha_sequence: str) -> str:
    result_sequence = []
    idx: int = 0
    while idx < len(alpha_sequence):
        current_char = alpha_sequence[idx]
        if current_char.isupper():
            result_sequence.append(current_char.lower())
        elif current_char.islower():
            result_sequence.append(current_char.upper())
        else:
            result_sequence.append(current_char)
        idx += 1
    return ''.join(result_sequence)