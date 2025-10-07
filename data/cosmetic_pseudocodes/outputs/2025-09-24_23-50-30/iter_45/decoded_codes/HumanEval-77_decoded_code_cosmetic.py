import math

def iscube(integer_value: int) -> bool:
    positive_variant: int = integer_value
    if positive_variant < 0:
        positive_variant = -positive_variant

    estimation: int = math.floor(positive_variant ** (1 / 3) + 0.5)
    power_check: int = estimation * estimation * estimation

    return power_check == positive_variant