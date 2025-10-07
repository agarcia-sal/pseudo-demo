def next_smallest(lst):
    unique_elements = []
    for index in range(len(lst)):
        element = lst[index]
        found = False
        for unique_index in range(len(unique_elements)):
            if unique_elements[unique_index] == element:
                found = True
                break
        if not found:
            unique_elements.append(element)
    unique_elements.sort()
    if len(unique_elements) < 2:
        return None
    else:
        return unique_elements[1]