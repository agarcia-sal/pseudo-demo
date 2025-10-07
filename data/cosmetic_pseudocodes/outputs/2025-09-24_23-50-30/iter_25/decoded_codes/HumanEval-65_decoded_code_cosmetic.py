def circular_shift(num_value: int, num_rotation: int) -> str:
    str_form: str = str(num_value)
    if not (num_rotation <= len(str_form)):
        return str_form[::-1]
    pivot: int = len(str_form) - num_rotation
    part_one: str = str_form[pivot:]
    part_two: str = str_form[:pivot]
    return part_one + part_two