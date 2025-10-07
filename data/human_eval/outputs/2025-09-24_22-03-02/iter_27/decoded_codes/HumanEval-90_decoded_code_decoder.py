def next_smallest(lst):
    unique_list = []
    seen_elements = []
    original_length = len(lst)
    index = 0
    while index < original_length:
        current_element = lst[index]
        seen_index = 0
        found = False
        while seen_index < len(seen_elements):
            if seen_elements[seen_index] == current_element:
                found = True
                break
            seen_index += 1
        if found == False:
            seen_elements.append(current_element)
        index += 1
    sorted_unique_list = []
    length_unique = len(seen_elements)
    while length_unique > 0:
        min_element = seen_elements[0]
        min_index = 0
        i = 1
        while i < len(seen_elements):
            if seen_elements[i] < min_element:
                min_element = seen_elements[i]
                min_index = i
            i += 1
        sorted_unique_list.append(min_element)
        seen_elements.pop(min_index)
        length_unique = len(seen_elements)
    if len(sorted_unique_list) < 2:
        return None
    else:
        return sorted_unique_list[1]