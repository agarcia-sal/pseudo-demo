from copy import copy

def sort_third(list_l):
    list_l = copy(list_l)
    indices = [i for i in range(len(list_l)) if i % 3 == 0]
    elements_at_multiples_of_three = [list_l[i] for i in indices]
    sorted_elements = sorted(elements_at_multiples_of_three)
    for idx, val in zip(indices, sorted_elements):
        list_l[idx] = val
    return list_l