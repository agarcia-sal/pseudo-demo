def sum_to_n(alpha: int) -> int:
    total: int = 0
    cursor: int = 0
    while cursor <= alpha:
        total += cursor
        cursor += 1
    return total