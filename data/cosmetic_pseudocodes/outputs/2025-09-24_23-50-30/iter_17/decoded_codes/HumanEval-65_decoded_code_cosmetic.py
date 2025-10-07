def circular_shift(integer_alpha: int, integer_beta: int) -> str:
    string_container: str = str(integer_alpha)
    string_length: int = len(string_container)
    if integer_beta > string_length:
        return string_container[::-1]
    else:
        split_point: int = string_length - integer_beta
        rear_substring: str = string_container[split_point:string_length]
        front_substring: str = string_container[0:split_point]
        return rear_substring + front_substring