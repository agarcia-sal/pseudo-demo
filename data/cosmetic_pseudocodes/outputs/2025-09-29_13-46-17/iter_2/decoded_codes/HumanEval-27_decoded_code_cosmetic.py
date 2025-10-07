from typing import List

def flip_case(input_string: str) -> str:
    result_chars: List[str] = []
    index: int = 0

    def recurse_flip() -> None:
        nonlocal index
        if index >= len(input_string):
            return
        char: str = input_string[index]
        if char.isupper():
            char = char.lower()
        elif char.islower():
            char = char.upper()
        result_chars.append(char)
        index += 1
        recurse_flip()

    recurse_flip()
    return "".join(result_chars)