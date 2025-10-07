def string_xor(a: str, b: str) -> str:
    def xor(i: str, j: str) -> str:
        # Return '0' if both characters are the same, '1' otherwise
        return '0' if i == j else '1'

    # Compute XOR for each character pair and join the results into a string
    result = ''.join(xor(x, y) for x, y in zip(a, b))
    return result