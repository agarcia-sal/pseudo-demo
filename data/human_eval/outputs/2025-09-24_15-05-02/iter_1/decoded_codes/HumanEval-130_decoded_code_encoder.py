def tri(n):
    if n == 0:
        return [1]
    tri = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            tri.append(1 + i // 2)
        else:
            tri.append(tri[i-1] + tri[i-2] + (i + 3) // 2)
    return tri