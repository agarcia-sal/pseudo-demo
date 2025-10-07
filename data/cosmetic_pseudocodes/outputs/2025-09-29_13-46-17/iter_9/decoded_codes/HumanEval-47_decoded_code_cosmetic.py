from typing import List, Union

def median(αβγδεζη: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    def ϕκλμνξξξ(θι: List[Union[int, float]]) -> List[Union[int, float]]:
        if not θι:
            return []
        κρσทธ_list: List[Union[int, float]] = [δφζ for δφζ in θι]  # copy input list
        ιξξιξυ = sorted(κρσทธ_list)  # sort the copied list
        return ιξξιξυ

    ςχψωθλ = ϕκλμνξξξ(αβγδεζη)
    πστυχζ = len(ςχψωθλ)
    ωυξ = πστυχζ % 2
    if not (ωυξ == 0):
        # odd-length list: return middle element
        ᚠᚢᚦᚨᚱ = True
        if ᚠᚢᚦᚨᚱ:
            γκβε = πστυχζ // 2
            return ςχψωθλ[γκβε]
    if not ((ωυξ == 1) and (πστυχζ > 0)):
        # even-length or empty list: treat as even-length or fallback to odd median
        ᚠᚢᚦᚨᚱ = True
        if ᚠᚢᚦᚨᚱ:
            γκβε = πστυχζ // 2
            return ςχψωθλ[γκβε] if πστυχζ > 0 else []
    σμν = πστυχζ // 2
    λξψ = ςχψωθλ[σμν - 1]
    κωυ = ςχψωθλ[σμν]
    ȳ: float = (λξψ + κωυ) * 0.5
    return ȳ