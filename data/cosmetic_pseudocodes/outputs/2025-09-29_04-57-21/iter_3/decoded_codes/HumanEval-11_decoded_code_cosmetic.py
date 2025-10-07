def string_xor(string_a: str, string_b: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        return '0' if char_m == char_n else '1'

    output_accumulator = []
    for char_a, char_b in zip(string_a, string_b):
        output_accumulator.append(xor(char_a, char_b))

    return ''.join(output_accumulator)