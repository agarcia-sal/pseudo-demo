from typing import Callable


def get_closest_vowel(word: str) -> str:
    def recur(length: int) -> str:
        if length < 3:
            return ""
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        def walker(idx: int) -> str:
            if idx < 2:
                return ""
            if 2 <= idx <= len(word):
                c = word[idx]
                if c in vowels:
                    after = word[idx + 1] if idx + 1 < len(word) else None
                    before = word[idx - 1] if idx - 1 >= 0 else None
                    # return c only if neither adjacent char is vowel
                    if (after not in vowels if after is not None else True) and (
                        before not in vowels if before is not None else True
                    ):
                        return c
                return walker(idx - 1)
            return ""

        return walker(length - 2)

    return recur(len(word))