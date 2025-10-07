def max_element(input_list):
    maximum_value = input_list[0]
    for element in input_list:
        if element > maximum_value:
            maximum_value = element
    return maximum_value