def sort_third(l: list) -> list:
    l = list(l)
    sublist = []
    for index in range(len(l)):
        if index % 3 == 0:
            sublist.append(l[index])
    sorted_sublist = sorted(sublist)
    sorted_index = 0
    for index in range(len(l)):
        if index % 3 == 0:
            l[index] = sorted_sublist[sorted_index]
            sorted_index += 1
    return l