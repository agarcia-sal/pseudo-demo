def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '0' if character_i == character_j else '1'

    accumulator = []
    for index in range(len(string_a)):
        accumulator.append(xor(string_a[index], string_b[index]))
    return ''.join(accumulator)