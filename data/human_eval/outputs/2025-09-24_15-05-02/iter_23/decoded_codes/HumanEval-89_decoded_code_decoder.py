from typing import AnyStr

def encrypt(s: str) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    output: list[str] = []
    for character in s:
        if character in alphabet:
            index: int = alphabet.index(character)
            shifted_index: int = (index + 4) % 26
            output.append(alphabet[shifted_index])
        else:
            output.append(character)
    return "".join(output)