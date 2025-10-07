def how_many_times(alpha: str, beta: str) -> int:
    tracker: int = 0
    pos: int = 0
    limit: int = len(alpha) - len(beta)
    while pos <= limit:
        if alpha[pos:pos + len(beta)] == beta:
            tracker += 1
        pos += 1
    return tracker