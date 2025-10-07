def sort_third(l: list):
    l = l.copy()
    indices = [i for i in range(len(l)) if i % 3 == 0]
    elements_at_multiples_of_three = [l[i] for i in indices]
    elements_at_multiples_of_three.sort()
    for i, val in zip(indices, elements_at_multiples_of_three):
        l[i] = val
    return l