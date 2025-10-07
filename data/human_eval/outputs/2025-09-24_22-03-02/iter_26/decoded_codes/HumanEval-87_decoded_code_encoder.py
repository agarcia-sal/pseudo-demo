def get_row(lst, x):
    coords = [(i, j) for i, row in enumerate(lst) for j, element in enumerate(row) if element == x]
    coords_sorted_by_column_desc = []
    for current in coords:
        inserted = False
        for m, compare in enumerate(coords_sorted_by_column_desc):
            if current[1] > compare[1]:
                coords_sorted_by_column_desc.insert(m, current)
                inserted = True
                break
        if not inserted:
            coords_sorted_by_column_desc.append(current)
    coords_sorted_final = []
    for current in coords_sorted_by_column_desc:
        inserted = False
        for q, compare in enumerate(coords_sorted_final):
            if current[0] < compare[0]:
                coords_sorted_final.insert(q, current)
                inserted = True
                break
        if not inserted:
            coords_sorted_final.append(current)
    return coords_sorted_final