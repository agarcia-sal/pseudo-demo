def get_row(lst, x):
    coords = []
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if lst[i][j] == x:
                coords.append((i, j))
            j += 1
        i += 1
    coords = sorted(coords, key=lambda t: t[1], reverse=True)
    coords = sorted(coords, key=lambda t: t[0])
    return coords