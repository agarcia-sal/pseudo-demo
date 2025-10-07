def solution(lst):
    sum_of_odd_elements_in_even_positions = 0
    for index, element in enumerate(lst):
        if index % 2 == 0 and element % 2 == 1:
            sum_of_odd_elements_in_even_positions += element
    return sum_of_odd_elements_in_even_positions