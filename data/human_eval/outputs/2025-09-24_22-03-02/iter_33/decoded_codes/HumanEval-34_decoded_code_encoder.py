def unique(l: list) -> list:
    temp_set = set()
    index = 0
    while index < len(l):
        temp_set.add(l[index])
        index += 1
    temp_list = []
    for element in temp_set:
        temp_list.append(element)
    sorted_list = sorted(temp_list)
    return sorted_list