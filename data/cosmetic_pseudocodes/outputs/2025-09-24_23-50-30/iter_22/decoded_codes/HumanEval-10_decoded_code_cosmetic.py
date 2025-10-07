from typing import List


def is_palindrome(word: str) -> bool:
    index_a: int = 0
    index_b: int = len(word) - 1
    while index_a < index_b:
        if word[index_a] != word[index_b]:
            return False
        index_a += 1
        index_b -= 1
    return True


def make_palindrome(sequence: str) -> str:
    if len(sequence) == 0:
        return ""

    for pos in range(len(sequence)):
        if is_palindrome(sequence[pos:]):
            prefix: str = sequence[:pos]
            reversed_prefix: List[str] = []
            for i in range(len(prefix) - 1, -1, -1):
                reversed_prefix.append(prefix[i])
            return sequence + "".join(reversed_prefix)
    return sequence  # case if nothing found, fallback to sequence itself