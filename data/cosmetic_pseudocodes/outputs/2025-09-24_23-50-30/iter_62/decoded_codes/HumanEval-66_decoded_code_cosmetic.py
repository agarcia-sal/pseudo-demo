def digitSum(alpha_seq: str) -> int:
    if not alpha_seq:
        return 0

    def recur(idx: int, accum: int) -> int:
        if idx == len(alpha_seq):
            return accum
        new_accum = accum + (ord(alpha_seq[idx]) if 'A' <= alpha_seq[idx] <= 'Z' else 0)
        return recur(idx + 1, new_accum)

    return recur(0, 0)