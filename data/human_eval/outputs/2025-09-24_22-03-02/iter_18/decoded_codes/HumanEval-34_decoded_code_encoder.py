def unique(l: list) -> list:
    unique_elements = []
    set_of_elements = []
    for index in range(len(l)):
        current_element = l[index]
        element_found = False
        for set_index in range(len(set_of_elements)):
            if set_of_elements[set_index] == current_element:
                element_found = True
                break
        if not element_found:
            set_of_elements.append(current_element)
    for i in range(len(set_of_elements)):
        unique_elements.append(set_of_elements[i])
    for i in range(len(unique_elements) - 1):
        for j in range(len(unique_elements) - 1 - i):
            if unique_elements[j] > unique_elements[j + 1]:
                temp = unique_elements[j]
                unique_elements[j] = unique_elements[j + 1]
                unique_elements[j + 1] = temp
    return unique_elements