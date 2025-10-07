def string_xor(string_a: str, string_b: str) -> str:
    def xor(char1: str, char2: str) -> str:
        return '1' if char1 != char2 else '0'

    return ''.join(xor(a, b) for a, b in zip(string_a, string_b))