def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            value = 1 + (i // 2)
            my_tri.append(value)
        else:
            value1 = my_tri[i - 1]
            value2 = my_tri[i - 2]
            value3 = (i + 3) // 2
            sum_value = value1 + value2 + value3
            my_tri.append(sum_value)
    return my_tri