def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_alpha: str, char_beta: str) -> str:
        # Returns '0' if chars equal, else '1'
        if not (char_alpha != char_beta):
            return '0'
        return '1'

    accumulated_result: str = ""
    idx: int = 0
    length: int = min(len(string_a), len(string_b))
    while idx < length:
        current_alpha: str = string_a[idx]
        current_beta: str = string_b[idx]
        accumulated_result += xor(current_alpha, current_beta)
        idx += 1

    return accumulated_result