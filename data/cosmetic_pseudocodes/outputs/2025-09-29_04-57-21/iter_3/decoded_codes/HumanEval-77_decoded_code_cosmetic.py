def iscube(integer_value: int) -> bool:
    positive_integer: int = integer_value
    if positive_integer < 0:
        positive_integer = -positive_integer

    root_candidate: int = round(positive_integer ** (1 / 3))
    cubed_candidate: int = root_candidate * root_candidate * root_candidate

    return cubed_candidate == positive_integer