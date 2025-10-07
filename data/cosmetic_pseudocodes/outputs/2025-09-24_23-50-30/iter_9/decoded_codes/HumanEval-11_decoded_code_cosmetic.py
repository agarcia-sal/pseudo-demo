from typing import List

def string_xor(string_p: str, string_q: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        # Return '0' if chars are equal, else '1'
        if not (char_m != char_n):
            return '0'
        return '1'

    accumulated: List[str] = []
    index_tracker: int = 0
    while index_tracker < len(string_p):
        acc_value: str = xor(string_p[index_tracker], string_q[index_tracker])
        accumulated.append(acc_value)
        index_tracker += 1

    return ''.join(accumulated)