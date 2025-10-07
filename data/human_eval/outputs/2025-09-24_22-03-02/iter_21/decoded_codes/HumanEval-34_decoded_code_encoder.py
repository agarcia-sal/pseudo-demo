def unique(l: list) -> list:
    temp_set = set()
    for element in l:
        temp_set.add(element)
    temp_list = []
    for element in temp_set:
        temp_list.append(element)
    temp_list.sort()
    return temp_list