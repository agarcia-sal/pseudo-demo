def sort_third(l: list) -> list:
    l = list(l)
    elements = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_elements = sorted(elements)
    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = sorted_elements[i // 3]
    return l