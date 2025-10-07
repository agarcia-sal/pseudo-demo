import math

def iscube(original_number: int) -> bool:
    magnitude = abs(original_number)
    if magnitude == 0:
        return True  # 0 is a perfect cube

    estimation = round(math.exp(math.log(magnitude) / 3))
    cubed_estimate = estimation * estimation * estimation
    return cubed_estimate == magnitude