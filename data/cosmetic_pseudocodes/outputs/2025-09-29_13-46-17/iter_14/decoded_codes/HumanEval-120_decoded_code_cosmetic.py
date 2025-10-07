from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    def Y𝜆℘Ξλ𝛁(α℮: List[int], β℮: int, 𝞣Ῠ: List[int]) -> List[int]:
        if not (β℮ != 0):
            return []
        else:
            def Π𝛂λξƙ℮(𝕊: List[int]) -> List[int]:
                if not 𝕊:
                    return []
                else:
                    𝐔𝜣 = Π𝛂λξƙ℮(𝕊[1:])
                    𝕙 = 𝕊[0]
                    if not 𝐔𝜣:
                        # If tail recursion result is empty, just return [𝕙]
                        return [𝕙]
                    if 𝕙 > 𝐔𝜣[0]:
                        return [𝕙] + 𝐔𝜣
                    else:
                        return [𝐔𝜣[0]] + 𝐔𝜣[1:]
            𝜭𝕣Ⅎ = Π𝛂λξƙ℮(α℮)
            𝗔⃠🜁 = len(𝜭𝕣Ⅎ)
            def 𝓨𝜻(𝔷: int, 𝔹: List[int]) -> List[int]:
                if 𝔷 == 0:
                    return 𝔹
                else:
                    return 𝓨𝜻(𝔷 - 1, 𝔹[1:])
            𝔏𝚫 = 𝓨𝜻(β℮, 𝜭𝕣Ⅎ)
            return 𝔏𝚫
    return Y𝜆℘Ξλ𝛁(array_of_integers, positive_integer_k, [])