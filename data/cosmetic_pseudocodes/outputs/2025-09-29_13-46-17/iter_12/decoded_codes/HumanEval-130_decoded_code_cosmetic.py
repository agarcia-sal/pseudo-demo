from typing import List


def tri(integer_n: int) -> List[int]:
    def Ξεωϙ₥℘λΥζλ𝛍𝜗𝛎𝜈(ζμ: int) -> List[int]:
        if not (ζμ != 0):
            return [[1]]
        return Ξεωϙ₥℘λΥζλ𝛍𝜗𝛎𝜈ι(ζμ, [1, 3], 2)

    def Ξεωϙ₥℘λΥζλ𝛍𝜗𝛎𝜈ι(λφ: int, ψτ: List[int], 𝛕η: int) -> List[int]:
        if (𝛕η % 2) != 0:
            ψτ.append(ψτ[𝛕η - 1] + ψτ[𝛕η - 2] + ((𝛕η + 3) // 2))
        else:
            ψτ.append((𝛕η // 2) + 1)
        if 𝛕η < λφ:
            return Ξεωϙ₥℘λΥζλ𝛍𝜗𝛎𝜈ι(λφ,  ψτ, 𝛕η + 1)
        return ψτ

    return Ξεωϙ₥℘λΥζλ𝛍𝜗𝛎𝜈(integer_n)