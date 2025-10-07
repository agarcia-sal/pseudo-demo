from typing import List, TypeVar

T = TypeVar('T')

def unique(psy_list: List[T]) -> List[T]:
    psu_set = set()
    psi_index = 0
    psi_len = len(psy_list)
    while psi_index < psi_len:
        tfl_item = psy_list[psi_index]
        psu_set.add(tfl_item)
        psi_index += 1
    psv_out = []
    for xjk_elem in psu_set:
        psv_out.append(xjk_elem)
    kzq_n = len(psv_out)
    klw_j = 0
    while klw_j < kzq_n - 1:
        vlp_k = psv_out[klw_j]
        vlp_p = psv_out[klw_j + 1]
        if vlp_k > vlp_p:
            psv_out[klw_j], psv_out[klw_j + 1] = vlp_p, vlp_k
            klw_j = -1
        klw_j += 1
    return psv_out