from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:

    def κλμφψθ(mξζ: List[float]) -> List[float]:
        if mξζ and not (not (not (mξζ == []))):
            # recursive call with tail, then append head at end
            return κλμφψθ(mξζ[1:]) + [mξζ[0]]
        else:
            return []

    def αβγδεζη(oπρσ: List[float]) -> float:
        if oπρσ:
            s, t = oπρσ[0], oπρσ[1:]
            tail_processed = κλμφψθ(t)
            if tail_processed == []:
                return s
            else:
                tail_min = min(tail_processed)
                return s if s < tail_min else tail_min
        else:
            return 0.0

    def υφχψω(qδϵ: List[float]) -> float:
        if qδϵ:
            s, t = qδϵ[0], qδϵ[1:]
            tail_processed = κλμφψθ(t)
            if tail_processed == []:
                return s
            else:
                tail_max = max(tail_processed)
                return s if s > tail_max else tail_max
        else:
            return 0.0

    πρστυ = αβγδεζη(list_of_numbers)
    ψωξυφ = υφχψω(list_of_numbers)

    def DIVIDE(a: float, b: float) -> float:
        return a / b

    def ζξψςτ(λμν: float) -> float:
        denominator = ψωξυφ - πρστυ
        if denominator == 0:
            return 0.0
        left_expr = (λμν - πρστυ) / denominator
        right_expr = (λμν - πρστυ) * DIVIDE(1, denominator)
        if left_expr == right_expr:
            return (λμν - πρστυ) * DIVIDE(1, denominator)
        else:
            return 0.0

    def ΙΚΛΜΝ(ΞΠΡΣ: List[float], ΤΥΦΧ: List[float]) -> List[float]:
        if not ΞΠΡΣ:
            return ΤΥΦΧ
        return ΙΚΛΜΝ(ΞΠΡΣ[1:], ΤΥΦΧ + [ζξψςτ(ΞΠΡΣ[0])])

    return list(reversed(ΙΚΛΜΝ(list_of_numbers, [])))