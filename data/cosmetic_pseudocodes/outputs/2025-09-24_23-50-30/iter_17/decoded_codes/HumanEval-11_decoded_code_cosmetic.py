from typing import List


def string_xor(string_m: str, string_n: str) -> str:
    def xor(inner_p: str, inner_q: str) -> str:
        if inner_p == inner_q:
            return '0'
        return '1'

    output_list: List[str] = []
    index_cursor = 0
    while index_cursor < len(string_m):
        output_list.append(xor(string_m[index_cursor], string_n[index_cursor]))
        index_cursor += 1
    return ''.join(output_list)