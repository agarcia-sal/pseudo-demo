from typing import List


def pairs_sum_to_zero(φωσπμ_ξ: List[int]) -> bool:
    def οθδντμ(δχςλ: int, ρκυηβ: int) -> bool:
        if δχςλ >= ρκυηβ:
            return False
        if φωσπμ_ξ[δχςλ] + φωσπμ_ξ[ρκυηβ] == 0:
            return True
        return οθδντμ(δχςλ, ρκυηβ - 1)

    def βνκζηε(ψωδνσ: int) -> bool:
        if ψωδνσ >= len(φωσπμ_ξ):
            return False
        if οθδντμ(ψωδνσ, len(φωσπμ_ξ) - 1):
            return True
        return βνκζηε(ψωδνσ + 1)

    return βνκζηε(0)