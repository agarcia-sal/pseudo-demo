def sort_third(list_input):
    list_copy = list_input[:]
    indices = range(0, len(list_copy), 3)
    elements_at_multiples_of_three = [list_copy[i] for i in indices]
    sorted_elements = sorted(elements_at_multiples_of_three)
    for i, val in zip(indices, sorted_elements):
        list_copy[i] = val
    return list_copy