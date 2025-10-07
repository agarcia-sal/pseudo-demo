from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    output_chars: List[str] = []
    for index_counter in range(len(string_a)):
        first_char = string_a[index_counter]
        second_char = string_b[index_counter]
        if not (first_char != second_char):
            output_chars.append('0')
        else:
            output_chars.append('1')
    return ''.join(output_chars)