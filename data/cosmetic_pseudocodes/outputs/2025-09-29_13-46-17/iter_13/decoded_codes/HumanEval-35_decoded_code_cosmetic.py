from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def ΞλΜβσ(υδφ: int, Ωτξ: List[T], σπλ: T) -> T:
        if υδφ != len(Ωτξ):
            if Ωτξ[υδφ] > σπλ:
                ret = ΞλΜβσ(υδφ + 1, Ωτξ, Ωτξ[υδφ])
            else:
                ret = ΞλΜβσ(υδφ + 1, Ωτξ, σπλ)
        else:
            ret = σπλ
        return ret

    ΡφπΚ = ΞλΜβσ(0, list_of_elements, list_of_elements[0])
    return ΡφπΚ