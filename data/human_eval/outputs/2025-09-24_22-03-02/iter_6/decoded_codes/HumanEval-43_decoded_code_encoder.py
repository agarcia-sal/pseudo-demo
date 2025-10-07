def pairs_sum_to_zero(input_list) -> bool:
    for index_one, element_one in enumerate(input_list):
        for index_two in range(index_one + 1, len(input_list)):
            if element_one + input_list[index_two] == 0:
                return True
    return False