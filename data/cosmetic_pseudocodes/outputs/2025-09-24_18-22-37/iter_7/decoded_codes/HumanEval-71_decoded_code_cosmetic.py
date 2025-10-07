from math import sqrt

def triangle_area(length_x: float, length_y: float, length_z: float) -> float:
    if (length_x + length_y) <= length_z:
        return -1
    if (length_x + length_z) <= length_y:
        return -1
    if (length_y + length_z) <= length_x:
        return -1

    total_half: float = (length_x + length_y + length_z) / 2
    part_a: float = total_half
    part_b: float = total_half - length_x
    part_c: float = total_half - length_y
    part_d: float = total_half - length_z

    intermediate_result: float = part_a * part_b * part_c * part_d
    root_value: float = sqrt(intermediate_result)
    final_result: float = round(root_value, 2)

    return final_result