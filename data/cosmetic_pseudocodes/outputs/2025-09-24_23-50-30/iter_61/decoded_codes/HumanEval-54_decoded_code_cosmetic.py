from typing import Set


def same_chars(alpha: str, beta: str) -> bool:
    CharSet = Set[str]

    def gather_chars(src: str, idx: int, collected: CharSet) -> CharSet:
        if idx >= len(src):
            return collected
        updated_set = collected | {src[idx]}
        return gather_chars(src, idx + 1, updated_set)

    setA = gather_chars(alpha, 0, set())
    setB = gather_chars(beta, 0, set())

    return setA == setB