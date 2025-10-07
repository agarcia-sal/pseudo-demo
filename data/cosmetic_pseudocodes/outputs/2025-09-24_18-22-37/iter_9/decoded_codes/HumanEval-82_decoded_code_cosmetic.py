def prime_length(input_string_parameter: str) -> bool:
    string_length_variable: int = len(input_string_parameter)
    if string_length_variable == 0 or string_length_variable == 1:
        return False
    divisor_counter: int = 2
    while divisor_counter < string_length_variable - 1:
        modulo_remainder: int = string_length_variable % divisor_counter
        if modulo_remainder == 0:
            return False
        divisor_counter += 1
    return True