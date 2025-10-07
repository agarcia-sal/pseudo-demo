def odd_count(list_of_strings):
    result_list = []
    for each_string in list_of_strings:
        odd_count = 0
        for each_character in each_string:
            if int(each_character) % 2 == 1:
                odd_count += 1
        message = "the number of odd elements " + str(odd_count) + "n the str" + str(odd_count) + "ng " + str(odd_count) + " of the " + str(odd_count) + "nput."
        result_list.append(message)
    return result_list