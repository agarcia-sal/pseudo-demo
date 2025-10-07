def unique(l: list):
    unique_set = set()
    for i in range(len(l)):
        unique_set.add(l[i])
    unique_list = []
    for element in unique_set:
        unique_list.append(element)
    sorted_list = sorted(unique_list)
    return sorted_list