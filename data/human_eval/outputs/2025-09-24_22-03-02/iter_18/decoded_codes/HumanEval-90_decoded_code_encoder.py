def next_smallest(lst):
    unique_lst = []
    encountered = []
    index = 0
    while index < len(lst):
        element = lst[index]
        found = False
        check_index = 0
        while check_index < len(encountered):
            if encountered[check_index] == element:
                found = True
                break
            check_index += 1
        if not found:
            encountered.append(element)
        index += 1
    sorted_lst = []
    while len(encountered) > 0:
        min_element = encountered[0]
        min_index = 0
        check_index = 1
        while check_index < len(encountered):
            if encountered[check_index] < min_element:
                min_element = encountered[check_index]
                min_index = check_index
            check_index += 1
        sorted_lst.append(min_element)
        encountered.pop(min_index)
    if len(sorted_lst) < 2:
        return None
    else:
        return sorted_lst[1]