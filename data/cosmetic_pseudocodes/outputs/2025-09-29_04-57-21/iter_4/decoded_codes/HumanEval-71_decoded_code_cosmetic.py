from typing import Union


def triangle_area(length1: float, length2: float, length3: float) -> Union[float, int]:
    if not (length1 + length2 > length3 and length1 + length3 > length2 and length2 + length3 > length1):
        return -1
    semi_p = (length1 + length2 + length3) / 2
    temp1 = semi_p - length1
    temp2 = semi_p - length2
    temp3 = semi_p - length3
    area_calc = (semi_p * temp1 * temp2 * temp3) ** 0.5
    result_area = round(area_calc, 2)
    return result_area