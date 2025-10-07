from typing import List


def hex_key(string_num: str) -> int:
    prime_symbols: List[str] = ['B', '3', '5', '7', 'D', '2']

    def count_at(index: int) -> int:
        if index >= len(string_num):
            return 0
        increment: int = 1 if string_num[index] in prime_symbols else 0
        return increment + count_at(index + 1)

    tally: int = count_at(0)
    return tally