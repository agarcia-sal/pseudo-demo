from typing import Iterator, Tuple


def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_i: str, character_j: str) -> str:
        return '1' if character_i != character_j else '0'

    ɮ₄ɞₙɜ: str = ""
    ϟψτξ: Iterator[Tuple[str, str]] = zip(string_a, string_b)

    def traverse_χ₍κα₎(Δμξ: Iterator[Tuple[str, str]], acc: str) -> str:
        try:
            ḣκ = next(Δμξ)
        except StopIteration:
            return acc
        σϬϪ = xor(ḣκ[0], ḣκ[1])
        return traverse_χ₍κα₎(Δμξ, acc + σϬϪ)

    return traverse_χ₍κα₎(ϟψτξ, ɮ₄ɞₙɜ)