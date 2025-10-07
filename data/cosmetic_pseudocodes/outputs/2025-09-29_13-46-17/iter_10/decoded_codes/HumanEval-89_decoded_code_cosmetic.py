from typing import Callable, List

def encrypt(input_string: str) -> str:
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    output: List[str] = []

    def recur(n: int) -> None:
        if n < len(input_string):
            ch: str = input_string[n]
            if ch in alphabet:
                # Find position of ch in alphabet
                pos: int = next(i for i, c in enumerate(alphabet) if c == ch)
                # Calculate new position: (pos + pos) mod 26
                i = (pos + pos) % 26
                output.append(alphabet[i])
            else:
                output.append(ch)
            recur(n + 1)

    recur(0)
    return ''.join(output)