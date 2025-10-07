def string_sequence(n: int) -> str:
    sequence = []
    i = 0
    while i <= n:
        element = str(i)
        sequence.append(element)
        i += 1
    result = ' '.join(sequence)
    return result