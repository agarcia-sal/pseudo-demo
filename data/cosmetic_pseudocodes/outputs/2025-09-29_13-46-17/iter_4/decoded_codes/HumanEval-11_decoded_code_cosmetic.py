from typing import Iterator

def string_xor(string_a: str, string_b: str) -> str:
    def diff_bit(bit_m: str, bit_n: str) -> str:
        return '1' if bit_m != bit_n else '0'

    def loop_zipper(iterator_p: Iterator[str], iterator_q: Iterator[str], acc: str) -> str:
        try:
            head_p = next(iterator_p)
            head_q = next(iterator_q)
        except StopIteration:
            return acc
        return loop_zipper(iterator_p, iterator_q, acc + diff_bit(head_p, head_q))

    return loop_zipper(iter(string_a), iter(string_b), '')