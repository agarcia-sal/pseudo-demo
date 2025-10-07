def add_elements(array_of_integers, integer_k):
    sum_result = 0
    for index in range(min(integer_k, len(array_of_integers))):
        element = array_of_integers[index]
        element_length = len(str(element))
        if element_length <= 2:
            sum_result += element
    return sum_result