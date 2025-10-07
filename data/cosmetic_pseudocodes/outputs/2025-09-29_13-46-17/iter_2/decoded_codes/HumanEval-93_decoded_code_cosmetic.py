from typing import Dict


def encode(message: str) -> str:
    vowels: str = "AEIOUaeiou"
    vowels_replace: Dict[str, str] = {}

    def add_mappings(i: int) -> None:
        if i == len(vowels):
            return
        c = vowels[i]
        vowels_replace[c] = chr(ord(c) + 2)
        add_mappings(i + 1)

    add_mappings(0)

    swapped_message = []
    index = 0
    while index < len(message):
        c = message[index]
        swapped_message.append(c.upper() if c.islower() else c.lower())
        index += 1
    swapped_message_str = "".join(swapped_message)

    def map_chars(idx: int) -> str:
        if idx == len(swapped_message_str):
            return ""
        current_char = swapped_message_str[idx]
        if current_char in vowels_replace:
            return vowels_replace[current_char] + map_chars(idx + 1)
        return current_char + map_chars(idx + 1)

    return map_chars(0)