def next_smallest(lst):
    unique_elements = []
    for element in lst:
        found = False
        for u in unique_elements:
            if u == element:
                found = True
                break
        if not found:
            unique_elements.append(element)
    sorted_elements = []
    while unique_elements:
        min_element = unique_elements[0]
        min_index = 0
        for k in range(1, len(unique_elements)):
            if unique_elements[k] < min_element:
                min_element = unique_elements[k]
                min_index = k
        sorted_elements.append(min_element)
        unique_elements.pop(min_index)
    if len(sorted_elements) < 2:
        return None
    else:
        return sorted_elements[1]