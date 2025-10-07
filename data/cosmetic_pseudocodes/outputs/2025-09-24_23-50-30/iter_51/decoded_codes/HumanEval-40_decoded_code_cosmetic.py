from typing import List

def triples_sum_to_zero(array_param: List[int]) -> bool:
    def loop_i(counter_i: int) -> bool:
        if counter_i > len(array_param) - 1:
            return False
        else:
            def loop_j(counter_j: int) -> bool:
                if counter_j > len(array_param) - 1:
                    return loop_i(counter_i + 1)
                else:
                    def loop_k(counter_k: int) -> bool:
                        if counter_k > len(array_param) - 1:
                            return loop_j(counter_j + 1)
                        else:
                            if array_param[counter_k] + array_param[counter_i] + array_param[counter_j] == 0:
                                return True
                            else:
                                return loop_k(counter_k + 1)
                    return loop_k(counter_j + 1)
            return loop_j(counter_i + 1)
    return loop_i(0)