from typing import Dict, List

def encode(message: str) -> str:
    vowels_map: Dict[str, str] = {}
    vowel_chars: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def build_map(index: int) -> None:
        if index == len(vowel_chars):
            return
        ch = vowel_chars[index]
        vowels_map[ch] = chr(ord(ch) + 2)
        build_map(index + 1)

    build_map(0)

    toggled: List[str] = []
    for i in range(len(message) - 1, -1, -1):
        toggled = [message[i].swapcase()] + toggled

    result: str = ""
    for each_char in toggled:
        if each_char not in vowels_map:
            result += each_char
        else:
            result += vowels_map[each_char]

    return result