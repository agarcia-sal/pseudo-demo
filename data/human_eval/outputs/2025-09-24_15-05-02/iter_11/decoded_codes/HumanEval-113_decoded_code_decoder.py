def odd_count(list_of_strings):
    result_list = []
    for string_element in list_of_strings:
        odd_count = sum(1 for digit in string_element if digit.isdigit() and int(digit) % 2 == 1)
        result_list.append("the number of odd elements " + str(odd_count) + "n the str" + str(odd_count) + "ng " + str(odd_count) + " of the " + str(odd_count) + "nput.")
    return result_list