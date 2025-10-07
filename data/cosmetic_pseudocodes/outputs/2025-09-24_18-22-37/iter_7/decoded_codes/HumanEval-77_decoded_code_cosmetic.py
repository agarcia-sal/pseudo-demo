from math import pow

def iscube(number_input: int) -> bool:
    positive_number: int = int(number_input)
    if positive_number < 0:
        positive_number = -positive_number

    root_estimate: int = round(pow(positive_number, 1/3))
    root_value: int = root_estimate
    final_cube: int = int(pow(root_value, 3))

    return final_cube == positive_number