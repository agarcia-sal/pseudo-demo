def odd_count(list_of_strings):
    result_list = []
    for string_element in list_of_strings:
        count_odd = 0
        for character in string_element:
            if int(character) % 2 == 1:
                count_odd += 1
        formatted_string = (
            "the number of odd elements " + str(count_odd) +
            "n the str" + str(count_odd) +
            "ng " + str(count_odd) +
            " of the " + str(count_odd) +
            "nput."
        )
        result_list.append(formatted_string)
    return result_list