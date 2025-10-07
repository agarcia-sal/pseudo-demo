from typing import Set


def vowels_count(text_value: str) -> int:
    letter_collection: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def tally(letters: str, idx: int, count_acc: int) -> int:
        if idx > len(letters):
            return count_acc
        current_char = letters[idx - 1]
        increase = 1 if current_char in letter_collection else 0
        return tally(letters, idx + 1, count_acc + increase)

    total_vowels = tally(text_value, 1, 0)
    if text_value and text_value[-1] in {"y", "Y"}:
        total_vowels += 1
    return total_vowels