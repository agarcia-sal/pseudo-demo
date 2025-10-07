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
    temp_sorted_coords = []
    index = 0
    while index < len(coords):
        current_element = coords[index]
        inserted = False
        insert_index = 0
        while insert_index < len(temp_sorted_coords) and not inserted:
            if current_element[1] > temp_sorted_coords[insert_index][1]:
                temp_sorted_coords.insert(insert_index, current_element)
                inserted = True
            insert_index += 1
        if not inserted:
            temp_sorted_coords.append(current_element)
        index += 1
    final_sorted_coords = []
    index2 = 0
    while index2 < len(temp_sorted_coords):
        current_element2 = temp_sorted_coords[index2]
        inserted2 = False
        insert_index2 = 0
        while insert_index2 < len(final_sorted_coords) and not inserted2:
            if current_element2[0] < final_sorted_coords[insert_index2][0]:
                final_sorted_coords.insert(insert_index2, current_element2)
                inserted2 = True
            insert_index2 += 1
        if not inserted2:
            final_sorted_coords.append(current_element2)
        index2 += 1
    return final_sorted_coords