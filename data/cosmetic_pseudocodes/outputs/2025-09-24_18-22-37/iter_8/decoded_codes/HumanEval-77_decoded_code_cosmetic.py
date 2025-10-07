def iscube(number_input: int) -> bool:
    modulus_variable = abs(number_input)
    root_guess = round(modulus_variable ** (1.0 / 3.0))
    cube_calc = 1
    counter_temp = 0
    while counter_temp < 3:
        cube_calc *= root_guess
        counter_temp += 1
    return cube_calc == modulus_variable