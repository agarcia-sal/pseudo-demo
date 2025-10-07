from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    def check_from(k_current: int) -> bool:
        if k_current < len(list_of_integers):
            elem_outer = list_of_integers[k_current]

            def inner_loop(m_current: int) -> bool:
                if m_current < len(list_of_integers):
                    elem_inner = list_of_integers[m_current]
                    if (elem_outer + elem_inner) == 0:
                        return True
                    else:
                        return inner_loop(m_current + 1)
                else:
                    return False

            if inner_loop(k_current + 1):
                return True
            else:
                return check_from(k_current + 1)
        else:
            return False

    return check_from(0)