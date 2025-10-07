def get_row(lst, x):
    coords = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))

    coords_sorted_by_column_desc = sorted(coords, key=lambda c: c[1], reverse=True)
    coords_sorted = sorted(coords_sorted_by_column_desc, key=lambda c: c[0])
    return coords_sorted