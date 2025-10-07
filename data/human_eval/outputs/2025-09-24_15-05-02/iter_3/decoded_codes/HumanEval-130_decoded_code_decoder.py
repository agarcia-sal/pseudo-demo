def tri(n):
    if n == 0:
        return [1]

    my_tribonacci_sequence = [1, 3]

    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tribonacci_sequence.append(1 + i // 2)
        else:
            value = my_tribonacci_sequence[i - 1] + my_tribonacci_sequence[i - 2] + ((i + 3) // 2)
            my_tribonacci_sequence.append(value)

    return my_tribonacci_sequence