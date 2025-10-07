def get_row(lst, x):
    coords = []
    i = 0
    while i < len(lst):
        row = lst[i]
        j = 0
        while j < len(row):
            element = row[j]
            if element == x:
                coords.append((i, j))
            j += 1
        i += 1

    coords_sorted_by_column_desc = []
    indices_column_desc = list(range(len(coords)))
    while len(indices_column_desc) > 0:
        max_index = indices_column_desc[0]
        k = 1
        while k < len(indices_column_desc):
            current_index = indices_column_desc[k]
            max_column = coords[max_index][1]
            current_column = coords[current_index][1]
            if current_column > max_column:
                max_index = current_index
            k += 1
        coords_sorted_by_column_desc.append(coords[max_index])
        indices_column_desc.remove(max_index)

    coords_sorted_by_row_asc = []
    indices_row_asc = list(range(len(coords_sorted_by_column_desc)))
    while len(indices_row_asc) > 0:
        min_index = indices_row_asc[0]
        k = 1
        while k < len(indices_row_asc):
            current_index = indices_row_asc[k]
            min_row = coords_sorted_by_column_desc[min_index][0]
            current_row = coords_sorted_by_column_desc[current_index][0]
            if current_row < min_row:
                min_index = current_index
            k += 1
        coords_sorted_by_row_asc.append(coords_sorted_by_column_desc[min_index])
        indices_row_asc.remove(min_index)

    return coords_sorted_by_row_asc