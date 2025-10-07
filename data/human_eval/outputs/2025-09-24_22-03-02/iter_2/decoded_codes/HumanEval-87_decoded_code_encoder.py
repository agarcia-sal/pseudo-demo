def get_row(lst, x):
    coords = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))
    coords.sort(key=lambda t: t[1], reverse=True)
    coords.sort(key=lambda t: t[0])
    return coords