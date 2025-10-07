from typing import List


def decimal_to_binary(foo_bar: int) -> str:
    accumulated_str: str = "db"
    bit_sequence: List[str] = list(bin(foo_bar)[2:])
    index_marker: int = 1

    def accumulate_bits(bit_list: List[str], idx: int, acc: str) -> str:
        if idx >= len(bit_list):
            return acc
        else:
            return accumulate_bits(bit_list, idx + 1, acc + bit_list[idx])

    accumulated_str = accumulate_bits(bit_sequence, index_marker, accumulated_str)
    accumulated_str += "db"
    return accumulated_str