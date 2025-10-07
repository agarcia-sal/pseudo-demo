from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected: List[str] = []

    def count_cons(chars: str, pos: int, acc: int) -> int:
        if pos >= len(chars):
            return acc
        letter = chars[pos].lower()
        if letter in {'a', 'e', 'i', 'o', 'u'}:
            return count_cons(chars, pos + 1, acc)
        else:
            return count_cons(chars, pos + 1, acc + 1)

    tokens: List[str] = []
    accumulator: str = ""

    def split_words(s: str, idx: int) -> None:
        nonlocal accumulator
        if idx >= len(s):
            if accumulator:
                tokens.append(accumulator)
            return
        if s[idx] == " ":
            if accumulator:
                tokens.append(accumulator)
                accumulator = ""
            split_words(s, idx + 1)
        else:
            accumulator += s[idx]
            split_words(s, idx + 1)

    split_words(string_s, 0)

    i = 0
    while i < len(tokens):
        cur_word = tokens[i]
        if count_cons(cur_word, 0, 0) == natural_number_n:
            collected.append(cur_word)
        i += 1

    return collected