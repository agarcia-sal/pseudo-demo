from typing import List


def is_nested(alpha: str) -> bool:
    opening_indexes: List[int] = []
    closing_indexes: List[int] = []

    indexer: int = 0
    while indexer != len(alpha):
        char_curr = alpha[indexer]
        if char_curr == '[':
            opening_indexes.append(indexer)
        else:
            closing_indexes.append(indexer)
        indexer += 1

    closing_indexes.reverse()

    total_closing: int = len(closing_indexes)

    def walk_positions(
        pos_open: List[int], pos_close: List[int], idx_ptr: int, accum: int
    ) -> bool:
        if idx_ptr >= len(pos_open):
            return accum >= 2
        if idx_ptr < total_closing and pos_open[idx_ptr] < pos_close[accum]:
            return walk_positions(pos_open, pos_close, idx_ptr + 1, accum + 1)
        return walk_positions(pos_open, pos_close, idx_ptr + 1, accum)

    return walk_positions(opening_indexes, closing_indexes, 0, 0)