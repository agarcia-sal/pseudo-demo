from typing import Dict


def encode(message: str) -> str:
    vowels_set: str = "AEIOUaeiou"

    def shift_chars(chars: str, offset: int) -> Dict[str, str]:
        shifted_map: Dict[str, str] = {}
        for idx in range(len(chars)):
            ch = chars[idx]
            shifted_map[ch] = chr(ord(ch) + offset)
        return shifted_map

    vowel_shift_map: Dict[str, str] = shift_chars(vowels_set, 2)

    def swap_case_recursive(text: str, pos: int, acc: str) -> str:
        if pos == len(text):
            return acc
        current_char: str = text[pos]
        swapped_char: str = (
            current_char.lower() if current_char.isupper() else current_char.upper()
        )
        return swap_case_recursive(text, pos + 1, acc + swapped_char)

    swapped_message: str = swap_case_recursive(message, 0, "")

    def replace_chars$text(
        index: int, data: str, map_: Dict[str, str], vowels: str, acc: str
    ) -> str:
        if index == len(data):
            return acc
        char_to_check: str = data[index]
        if char_to_check in vowels:
            acc += map_[char_to_check]
        else:
            acc += char_to_check
        return replace_chars$text(index + 1, data, map_, vowels, acc)

    return replace_chars$text(0, swapped_message, vowel_shift_map, vowels_set, "")