def starts_one_ends(qr: int) -> int:
    if qr == 1:
        return 1
    else:
        return 18 * (10 ** (qr - 2))