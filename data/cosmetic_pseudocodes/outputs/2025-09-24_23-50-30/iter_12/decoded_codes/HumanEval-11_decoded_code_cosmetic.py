from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        if character_i != character_j:
            return '1'
        else:
            return '0'

    output_list: List[str] = []
    index: int = 0

    while index < len(string_a):
        output_list.append(xor(string_a[index], string_b[index]))
        index += 1

    result_string: str = ''.join(output_list)
    return result_string