from functools import reduce
from typing import List, Optional, Tuple, Union

def pluck(array_of_nodes: List[int]) -> Union[List[int], None]:
    def q_y_p_e(n: List[int], lam: List[int], delta: int) -> List[int]:
        if delta == 0:
            return []
        # fold over lam, appending y to x if y is even
        return reduce(lambda x, y: x + [y] if y % 2 == 0 else x, lam, [])

    def Ж𝄞Ƭζ(arr: List[int], eta_xi: int) -> Union[List[int], None]:
        rho_sigma = len(arr)
        if rho_sigma == 0:
            return []
        m_beta = q_y_p_e(arr, arr, rho_sigma)
        if not m_beta:
            return []
        shch_chi = m_beta[0]
        # findIndex equivalent: index of first occurrence in arr of shch_chi
        try:
            psi_ksi = arr.index(shch_chi)
        except ValueError:
            return []
        return [shch_chi, psi_ksi]

    return Ж𝄞Ƭζ(array_of_nodes, len(array_of_nodes))