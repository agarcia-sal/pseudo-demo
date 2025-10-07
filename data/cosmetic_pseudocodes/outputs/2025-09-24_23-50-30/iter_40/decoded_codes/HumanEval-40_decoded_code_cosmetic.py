from typing import List

def triples_sum_to_zero(array_data: List[int]) -> bool:
    length = len(array_data)

    def recursion_loop_XY(z1: int) -> bool:
        def recursion_loop_Y(z2: int) -> bool:
            def recursion_loop_Z(z3: int) -> bool:
                if z3 >= length:
                    return recursion_loop_Y(z2 + 1)
                if z2 >= length - 1:
                    return recursion_loop_XY(z1 + 1)
                if z1 >= length - 2:
                    return False
                if array_data[z1] + array_data[z2] + array_data[z3] == 0:
                    return True
                return recursion_loop_Z(z3 + 1)
            return recursion_loop_Z(z2 + 1)
        return recursion_loop_Y(z1 + 1)
    return recursion_loop_XY(0)