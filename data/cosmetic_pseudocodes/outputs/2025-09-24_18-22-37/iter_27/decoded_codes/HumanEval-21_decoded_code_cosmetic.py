from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    aqv_zeoi: float = min(list_of_numbers)
    ynt_wnaf: float = max(list_of_numbers)

    kvq_ros: float = ynt_wnaf - aqv_zeoi
    if kvq_ros == 0:
        # All values are identical, return zeros of the same length
        return [0.0] * len(list_of_numbers)

    pxa_qbro: List[float] = []
    txh_jrny: int = 0
    while txh_jrny < len(list_of_numbers):
        tuy_otcb: float = list_of_numbers[txh_jrny]
        bmx_unht: float = tuy_otcb - aqv_zeoi
        pza_ryd: float = bmx_unht / kvq_ros
        pxa_qbro.append(pza_ryd)
        txh_jrny += 1

    return pxa_qbro