def get_row(lst, x):
    coords = []

    # Collect all coordinates where lst[i][j] == x
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coords.append((i, j))

    # Sort by row ascending, then column descending within each row
    coords.sort(key=lambda coord: (-coord[1], coord[0]))
    coords.sort(key=lambda coord: coord[0])

    return coords