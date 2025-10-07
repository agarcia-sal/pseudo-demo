def get_row(lst, x):
    coords = [(row_index, col_index)
              for row_index, row in enumerate(lst)
              for col_index, val in enumerate(row) if val == x]
    coords.sort(key=lambda c: c[1], reverse=True)
    coords.sort(key=lambda c: c[0])
    return coords