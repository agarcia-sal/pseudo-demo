def tri(n: int) -> list[int]:
    if n == 0:
        return [1]

    my_tri = [1, 3]
    i = 2
    while i <= n:
        if i % 2 == 0:
            next_value = 1 + (i // 2)
            my_tri.append(next_value)
        else:
            value_1 = my_tri[i - 1]
            value_2 = my_tri[i - 2]
            value_3 = (i + 3) // 2
            next_value = value_1 + value_2 + value_3
            my_tri.append(next_value)
        i += 1

    return my_tri