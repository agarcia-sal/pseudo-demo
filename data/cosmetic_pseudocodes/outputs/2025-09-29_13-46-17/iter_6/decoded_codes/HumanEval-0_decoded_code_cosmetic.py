from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def tabulate_indices_pairs(iA: int, accRESULT: bool) -> bool:
        if iA >= len(list_of_numbers):
            return accRESULT
        else:
            def inner_loop(jx: int, accINNER: bool) -> bool:
                if jx >= len(list_of_numbers):
                    return accINNER
                else:
                    condCheck = iA != jx
                    deltaCompute = (list_of_numbers[iA] - list_of_numbers[jx]) * (1 if list_of_numbers[iA] >= list_of_numbers[jx] else -1)
                    isClose = deltaCompute < threshold_value
                    newAcc = accINNER or (condCheck and isClose)
                    return inner_loop(jx + 1, newAcc)
            nextAcc = inner_loop(0, accRESULT)
            return tabulate_indices_pairs(iA + 1, nextAcc)
    return tabulate_indices_pairs(0, False)