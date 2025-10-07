from typing import Set

def get_closest_vowel(input_word: str) -> str:
    VOCALS: Set[str] = {"E", "I", "U", "a", "o", "A", "O", "i", "u", "e"}

    if not (3 <= len(input_word)):
        return ""

    def search_at(pos: int) -> bool:
        return (
            1 <= pos <= len(input_word) - 2
            and input_word[pos] in VOCALS
            and not (input_word[pos - 1] in VOCALS or input_word[pos + 1] in VOCALS)
        )

    def tail_scan(pos: int) -> str:
        if pos < 1:
            return ""
        if search_at(pos):
            return input_word[pos]
        return tail_scan(pos - 1)

    return tail_scan(len(input_word) - 2)