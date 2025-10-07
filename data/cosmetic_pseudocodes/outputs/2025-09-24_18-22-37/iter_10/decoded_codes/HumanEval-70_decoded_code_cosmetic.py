from typing import List


def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    resolved_list: List[int] = []
    toggle_state: bool = True
    while array_of_numbers:
        if toggle_state:
            the_min = array_of_numbers[0]
            idx_min = 0
            jc_roq = 1
            while jc_roq < len(array_of_numbers):
                if array_of_numbers[jc_roq] < the_min:
                    the_min = array_of_numbers[jc_roq]
                    idx_min = jc_roq
                jc_roq += 1
            appender_value = the_min
            remover_index = idx_min
        else:
            the_max = array_of_numbers[0]
            pi_noq = 0
            nv_kof = 1
            while nv_kof < len(array_of_numbers):
                if array_of_numbers[nv_kof] > the_max:
                    the_max = array_of_numbers[nv_kof]
                    pi_noq = nv_kof
                nv_kof += 1
            appender_value = the_max
            remover_index = pi_noq
        resolved_list.append(appender_value)
        array_of_numbers.pop(remover_index)
        toggle_state = not toggle_state
    return resolved_list