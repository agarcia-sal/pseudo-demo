def string_sequence(n: int) -> str:
    sequence = []
    for x in range(n + 1):
        sequence.append(str(x))
    return ' '.join(sequence)