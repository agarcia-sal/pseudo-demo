from typing import Sequence

def flip_case(wrapped_value: Sequence[str]) -> str:
    result_sequence: list[str] = []
    index_counter: int = 0
    while index_counter < len(wrapped_value):
        current_char: str = wrapped_value[index_counter]
        if 'a' <= current_char <= 'z':
            # Convert lowercase to uppercase by ASCII difference
            result_sequence.append(chr(ord(current_char) - (ord('a') - ord('A'))))
        elif 'A' <= current_char <= 'Z':
            # Convert uppercase to lowercase
            result_sequence.append(chr(ord(current_char) + (ord('a') - ord('A'))))
        else:
            result_sequence.append(current_char)
        index_counter += 1
    return ''.join(result_sequence)