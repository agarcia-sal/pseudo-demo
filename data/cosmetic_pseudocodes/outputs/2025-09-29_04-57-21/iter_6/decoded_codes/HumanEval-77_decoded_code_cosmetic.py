from math import exp, log

def iscube(integer_value: int) -> bool:
    magnitude = integer_value
    if magnitude < 0:
        magnitude = -magnitude

    # Handle zero explicitly as log(0) is undefined
    if magnitude == 0:
        return True

    root_candidate = int(round(exp(log(magnitude) / 3)))
    candidate_cube = root_candidate * root_candidate * root_candidate
    return candidate_cube == magnitude