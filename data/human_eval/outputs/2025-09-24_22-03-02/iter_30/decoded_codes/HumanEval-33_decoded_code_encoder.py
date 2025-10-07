def sort_third(l: list):
    l = list(l)
    indices_to_sort = []
    values_to_sort = []
    length = len(l)
    index = 0
    while index < length:
        if index % 3 == 0:
            indices_to_sort.append(index)
            values_to_sort.append(l[index])
        index += 1
    sorted_values = sorted(values_to_sort)
    sorted_index = 0
    while sorted_index < len(indices_to_sort):
        l[indices_to_sort[sorted_index]] = sorted_values[sorted_index]
        sorted_index += 1
    return l