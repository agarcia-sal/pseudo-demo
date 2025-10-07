def iscube(input_number: int) -> bool:
    positive_number: int = input_number if input_number >= 0 else -input_number
    root_candidate: int = round(positive_number ** (1 / 3))
    powered_value: int = root_candidate * root_candidate * root_candidate
    return powered_value == positive_number