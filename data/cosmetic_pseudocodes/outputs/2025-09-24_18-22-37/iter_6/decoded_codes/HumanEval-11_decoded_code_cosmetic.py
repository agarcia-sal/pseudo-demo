def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    accumulator = []
    length_n = len(string_a)
    for index_m in range(length_n):
        accumulator.append(xor(string_a[index_m], string_b[index_m]))
    return ''.join(accumulator)