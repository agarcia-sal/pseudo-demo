def string_sequence(n: int) -> str:
    sequence = []
    i = 0
    while i <= n:
        str_i = str(i)
        sequence.append(str_i)
        i += 1
    result = " ".join(sequence)
    return result