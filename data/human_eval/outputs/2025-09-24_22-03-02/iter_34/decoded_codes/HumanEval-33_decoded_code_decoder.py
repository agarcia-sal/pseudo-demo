def sort_third(l: list) -> list:
    l = list(l)
    indices_to_sort = []
    length_of_l = len(l)
    for i in range(length_of_l):
        if i % 3 == 0:
            indices_to_sort.append(l[i])
    sorted_values = sorted(indices_to_sort)
    position_to_replace = 0
    for j in range(length_of_l):
        if j % 3 == 0:
            l[j] = sorted_values[position_to_replace]
            position_to_replace += 1
    return l