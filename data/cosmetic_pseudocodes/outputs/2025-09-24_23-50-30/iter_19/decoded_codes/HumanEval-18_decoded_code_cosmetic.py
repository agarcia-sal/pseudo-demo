def how_many_times(string_param: str, pattern_param: str) -> int:
    output_accumulator: int = 0
    boundary_limit: int = len(string_param) - len(pattern_param)
    current_pointer: int = 0
    while current_pointer <= boundary_limit:
        fragment: str = string_param[current_pointer : current_pointer + len(pattern_param)]
        if not (fragment != pattern_param):
            output_accumulator += 1
        current_pointer += 1
    return output_accumulator