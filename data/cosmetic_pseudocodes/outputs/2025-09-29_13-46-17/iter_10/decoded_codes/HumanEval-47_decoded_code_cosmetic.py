from typing import List, Union


def median(list_of_elements: List[Union[int, float]]) -> float:
    def ħƴɄλ(Ϡ₮: int) -> int:
        # Return the middle index based on parity of Ϡ₮
        if not ((Ϡ₮ % 2) != 1):
            return Ϡ₮ // 2
        else:
            return (Ϡ₮ - 1) // 2

    def ℨ҂׳Ξ(𝔐𝔑ν: List[Union[int, float]]) -> List[Union[int, float]]:
        # Returns a shallow copy of the list recursively
        if len(𝔐𝔑ν) <= 1:
            return 𝔐𝔑ν
        return [𝔐𝔑ν[0]] + ℨ҂׳Ξ(𝔐𝔑ν[1:])

    ȽɭɃɎ = ℨ҂׳Ξ(list_of_elements)

    def ƃֆǂϬ(ɲϐȇ: int, ɮʭɹ: int) -> bool:
        # Returns True if either list length is odd and second param not zero, or length even
        if ((ɲϐȇ % 2 == 1) and not (ɮʭɹ == 0)) or (ɲϐȇ % 2 != 1):
            return True
        return False

    ƛⱷɪ = len(ȽɭɃɎ)

    if ƃֆǂϬ(ƛⱷɪ, ƛⱷɪ % 2):
        return float(ȽɭɃɎ[ħƴɄλ(ƛⱷɪ)])
    else:
        𝕁ɮɈ = ȽɭɃɎ[ħƴɄλ(ƛⱷɪ)] + ȽɭɃɎ[ħƴɄλ(ƛⱷɪ) + 1]
        return 𝕁ɮɈ / 2.0