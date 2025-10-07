def how_many_times(alpha_string: str, beta_string: str) -> int:
    accumulator = 0
    upper_bound = len(alpha_string) - len(beta_string)
    position = 0
    while position <= upper_bound:
        segment = alpha_string[position:position + len(beta_string)]
        if segment == beta_string:
            accumulator += 1
        position += 1
    return accumulator