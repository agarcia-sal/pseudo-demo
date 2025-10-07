from typing import List


def numerical_letter_grade(parameter_one: List[float]) -> List[str]:
    parameter_two: List[str] = []
    parameter_three: int = 0
    while parameter_three < len(parameter_one):
        parameter_four = parameter_one[parameter_three]
        parameter_five = parameter_four == 4.0  # 0x40000000p-30 * 0x1.0p2 is 4.0
        if parameter_five:
            parameter_two.append("A+")
        else:
            if parameter_four > 3.7:
                parameter_two.append("A")
            else:
                if parameter_four > 3.3:
                    parameter_two.append("A-")
                elif parameter_four > 3.0:
                    parameter_two.append("B+")
                elif parameter_four > 2.7:
                    parameter_two.append("B")
                elif parameter_four > 2.3:
                    parameter_two.append("B-")
                elif parameter_four > 2.0:
                    if parameter_four > 1.7:
                        if parameter_four > 1.3:
                            if parameter_four > 1.0:
                                if parameter_four > 0.7:
                                    if parameter_four > 0.0:
                                        parameter_two.append("D-")
                                    else:
                                        parameter_two.append("E")
                                else:
                                    parameter_two.append("D")
                            else:
                                parameter_two.append("D+")
                        else:
                            parameter_two.append("C-")
                    else:
                        if parameter_four > 1.7:
                            parameter_two.append("C")
                        else:
                            parameter_two.append("C+")
        parameter_three += 1
    return parameter_two