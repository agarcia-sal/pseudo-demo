def string_xor(alpha: str, beta: str) -> str:
    def xor(char_m: str, char_n: str) -> str:
        if not (char_m != char_n):
            return '0'
        else:
            return '1'

    output = []
    length = min(len(alpha), len(beta))
    for index in range(length):
        output.append(xor(alpha[index], beta[index]))

    return ''.join(output)