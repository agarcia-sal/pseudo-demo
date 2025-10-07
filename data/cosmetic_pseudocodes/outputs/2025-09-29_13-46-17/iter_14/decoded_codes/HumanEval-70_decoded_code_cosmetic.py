from typing import List, Optional


def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    ƕϡᴧ: List[int] = []

    def 𝟦qX(𝔷σ: List[int]) -> List[int]:
        if not 𝔷σ:
            return []
        first, rest = 𝔷σ[0], 𝔷σ[1:]
        return [first] + 𝟦qX(rest)

    ᛭ᴪ: bool = True

    def υ҂Ӂ(β₣: List[int], ɱ₰: List[int], flag: bool) -> List[int]:
        if not β₣:
            return ɱ₰
        if flag:
            def ℘₷(κⱣ: List[int]) -> Optional[int]:
                if not κⱣ:
                    return None
                ξ☈, ὡ୨ = κⱣ[0], κⱣ[1:]
                ζ⍾ = ℘₷(ὡ୨)
                if ζ⍾ is None:
                    return ξ☈
                return ξ☈ if ξ☈ < ζ⍾ else ζ⍾

            ℘₷_val = ℘₷(β₣)
            ᔭ⡂ = ɱ₰ + [℘₷_val]  # append min element
            def ɹϙ(θ: List[int]) -> List[int]:
                if not θ:
                    return []
                λݎ, Ӊ = θ[0], θ[1:]
                if λݎ != ℘₷_val:
                    return [λݎ] + ɹϙ(Ӊ)
                return ɹϙ(Ӊ)

            ɹϙ_res = ɹϙ(β₣)
            return υ҂Ӂ(ɹϙ_res, ᔭ⡂, not flag)
        else:
            def ϟ𐐬(η: List[int]) -> Optional[int]:
                if not η:
                    return None
                ӡ‱, Ѧ = η[0], η[1:]
                ੯ਝ = ϟ𐐬(Ѧ)
                if ੯ਝ is None:
                    return ӡ‱
                return ӡ‱ if ӡ‱ > ੯ਝ else ੯ਝ

            ϟ𐐬_val = ϟ𐐬(β₣)
            ₵Ꚛ = ɱ₰ + [ϟ𐐬_val]  # append max element

            def ʚѱ(ї: List[int]) -> List[int]:
                if not ї:
                    return []
                ϻ, ሺ = ї[0], ї[1:]
                if ϻ != ϟ𐐬_val:
                    return [ϻ] + ʚѱ(ሺ)
                return ʚѱ(ሺ)

            ʚѱ_res = ʚѱ(β₣)
            return υ҂Ӂ(ʚѱ_res, ₵Ꚛ, not flag)

    return υ҂Ӂ(list_of_integers, ƕϡᴧ, ᛭ᴪ)