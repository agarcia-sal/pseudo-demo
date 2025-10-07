from typing import List

def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_p: str, char_q: str) -> str:
        # Return '0' if chars are equal, '1' otherwise
        return '0' if char_p == char_q else '1'
    res_list: List[str] = [
        xor(string_a[idx], string_b[idx]) for idx in range(len(string_a))
    ]
    return "".join(res_list)