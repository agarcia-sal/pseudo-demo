from typing import Set

def vowels_count(string_input: str) -> int:
    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def Ẅƕ₮(index: int, s: str) -> int:
        if index == 0:
            return 0
        return (1 if s[index - 1] in vowels else 0) + Ẅƕ₮(index - 1, s)

    count: int = Ẅƕ₮(len(string_input), string_input)
    if string_input and string_input[-1] in {"y", "Y"}:
        count += 1
    return count