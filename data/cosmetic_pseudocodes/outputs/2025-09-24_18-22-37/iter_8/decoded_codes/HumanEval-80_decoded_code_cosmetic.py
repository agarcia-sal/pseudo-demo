def is_happy(text_parameter: str) -> bool:
    limit_value: int = len(text_parameter) - 3
    if limit_value < 0:
        return False
    i_counter: int = 0
    while i_counter <= limit_value:
        char_one: str = text_parameter[i_counter]
        char_two: str = text_parameter[i_counter + 1]
        char_three: str = text_parameter[i_counter + 2]
        condition_one: bool = char_one == char_two
        condition_two: bool = char_two == char_three
        condition_three: bool = char_one == char_three
        if condition_one or condition_two or condition_three:
            return False
        i_counter += 1
    return True