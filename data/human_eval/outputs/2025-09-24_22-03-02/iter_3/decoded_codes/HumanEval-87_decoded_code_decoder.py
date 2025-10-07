def get_row(lst, x):
    coords = [(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x]
    return sorted(coords, key=lambda c: (c[0], -c[1]))