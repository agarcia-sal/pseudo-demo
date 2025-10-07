from typing import Dict


def encode(message: str) -> str:
    vowels_str: str = "aeiouAEIOU"
    shift_map: Dict[str, str] = {}
    counter: int = 0
    while counter < len(vowels_str):
        original_char: str = vowels_str[counter]
        shifted_char: str = chr(ord(original_char) + 2)
        shift_map[original_char] = shifted_char
        counter += 1

    def swapCase(inputStr: str) -> str:
        result: list[str] = []
        pos: int = 0
        while pos != len(inputStr):
            current_char: str = inputStr[pos]
            if current_char == current_char.upper():
                result.append(current_char.lower())
            else:
                result.append(current_char.upper())
            pos += 1
        return ''.join(result)

    flipped_message: str = swapCase(message)
    output: list[str] = []
    idx: int = 0
    for ch in flipped_message:
        if ch in shift_map:
            output.append(shift_map[ch])
        else:
            output.append(ch)
        idx += 1
    return ''.join(output)