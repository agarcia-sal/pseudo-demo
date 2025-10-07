from typing import List


def anti_shuffle(string_input: str) -> str:
    return " ".join("".join(sorted(word)) for word in string_input.split(" "))