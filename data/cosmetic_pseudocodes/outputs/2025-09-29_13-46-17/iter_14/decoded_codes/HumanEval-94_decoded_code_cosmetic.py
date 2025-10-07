from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def χϘλ(Ωδϡ: int, 𝜁ζ: int) -> int:
            if not (𝜁ζ * 𝜁ζ <= Ωδϡ):
                return 𝜁ζ
            else:
                return χϘλ(Ωδϡ, 𝜁ζ + 1)

        def ζ𝜊(Υθι: int, 𝜉συ: int) -> bool:
            if 𝜉συ > 1 and (Υθι % 𝜉συ) == 0:
                return False
            elif 𝜉συ > χϘλ(Υθι, 2):
                return True
            else:
                return ζ𝜊(Υθι, 𝜉συ + 1)

        if integer_value <= 1:
            return False
        return ζ𝜊(integer_value, 2)

    def λβζ(ξ: int, 𝜣: int) -> List[int]:
        if ξ >= 𝜣:
            return []
        else:
            return [ξ] + λβζ(ξ + 1, 𝜣)

    def 𝛼𝛽𝛾(ϙ: int, 𝛥: int, Ἂ: int) -> int:
        if Ἂ >= ϙ:
            return 𝛥
        else:
            ψ = 𝛥
            ω = Ἂ
            υ = 0
            if list_of_integers[Ἂ] > ψ and isPrime(list_of_integers[Ἂ]):
                υ = list_of_integers[Ἂ]
            else:
                υ = ψ
            return 𝛼𝛽𝛾(ϙ, υ, Ἂ + 1)

    ξϖϝ = 𝛼𝛽𝛾(len(list_of_integers), 0, 0)

    def εζη(υζθ: str) -> int:
        if υζθ == "":
            return 0
        else:
            return int(υζθ[0]) + εζη(υζθ[1:])

    return εζη(str(ξϖϝ))