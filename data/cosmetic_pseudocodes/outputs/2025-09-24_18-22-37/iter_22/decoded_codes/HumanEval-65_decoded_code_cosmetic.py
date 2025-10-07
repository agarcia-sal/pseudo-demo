def circular_shift(number_param: int, rotate_amount: int) -> str:
    temp_string = str(number_param)
    if rotate_amount > len(temp_string):
        return temp_string[::-1]
    split_index = len(temp_string) - rotate_amount
    part_one = temp_string[split_index:]
    part_two = temp_string[:split_index]
    return part_one + part_two