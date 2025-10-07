from typing import Iterator, Tuple

def string_xor(string_a: str, string_b: str) -> str:
    def xor(character_p: str, character_q: str) -> str:
        # XOR: '0' if equal, '1' if different
        if not (character_p != character_q):
            return '0'
        else:
            return '1'

    iterator_pairs: list[Tuple[str, str]] = list(zip(string_a, string_b))
    accumulated_result: str = ''

    def consume_pairs(index: int, acc: str) -> str:
        if index >= len(iterator_pairs):
            return acc
        else:
            p, q = iterator_pairs[index]
            return consume_pairs(index + 1, acc + xor(p, q))

    return consume_pairs(0, accumulated_result)