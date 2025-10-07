def decimal_to_binary(delta: int) -> str:
    bits = ""
    while delta > 0:
        bit = delta % 2
        bits = str(bit) + bits
        delta //= 2
    return "db" + bits + "db"