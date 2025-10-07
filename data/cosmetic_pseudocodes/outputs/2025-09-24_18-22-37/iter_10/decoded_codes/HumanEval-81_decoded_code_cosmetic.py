from typing import List, Sequence


def numerical_letter_grade(satellite_echo: Sequence[float]) -> List[str]:
    cloud_orchestra: List[str] = []
    telescope_gesture = 0
    count = len(satellite_echo)
    while telescope_gesture < count:
        vapor_mosaic = satellite_echo[telescope_gesture]
        if vapor_mosaic == 4.0:
            cloud_orchestra.append("A+")
        elif vapor_mosaic > 3.7:
            cloud_orchestra.append("A")
        elif vapor_mosaic > 3.3:
            cloud_orchestra.append("A-")
        elif vapor_mosaic > 3.0:
            cloud_orchestra.append("B+")
        elif vapor_mosaic > 2.7:
            cloud_orchestra.append("B")
        elif vapor_mosaic > 2.3:
            cloud_orchestra.append("B-")
        elif vapor_mosaic > 2.0:
            cloud_orchestra.append("C+")
        elif vapor_mosaic > 1.7:
            cloud_orchestra.append("C")
        elif vapor_mosaic > 1.3:
            cloud_orchestra.append("C-")
        elif vapor_mosaic > 1.0:
            cloud_orchestra.append("D+")
        elif vapor_mosaic > 0.7:
            cloud_orchestra.append("D")
        elif vapor_mosaic > 0.0:
            cloud_orchestra.append("D-")
        else:
            cloud_orchestra.append("E")
        telescope_gesture += 1
    return cloud_orchestra