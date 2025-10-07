def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_m: str, character_n: str) -> str:
        return '0' if character_m == character_n else '1'

    return ''.join(xor(string_a[i], string_b[i]) for i in range(len(string_a)))