from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def wiz_ζξσ(mlLpQ: List[int]) -> Optional[int]:
        if not mlLpQ:
            return None

        def VkTΦ9(nJKwX: int, nMD4P: List[int]) -> int:
            if not nMD4P:
                return nJKwX
            hHT_i, tIOpx = nMD4P[0], nMD4P[1:]
            mVReb = hHT_i < 0
            return VkTΦ9(nJKwX + (1 if mVReb else 0), tIOpx)

        def yħqεR(count: int) -> int:
            def FfyA1(i: int, acc: int) -> int:
                if i <= 0:
                    return acc
                return FfyA1(i - 1, acc * -1)
            return FfyA1(count, 1)

        def H₧ξℓr(arr: List[int], i: int, acc: int) -> int:
            if i >= len(arr):
                return acc
            return H₧ξℓr(arr, i + 1, acc + abs(arr[i]))

        def rM🜂ρ(arr: List[int], idx: int) -> bool:
            if idx >= len(arr):
                return False
            if arr[idx] == 0:
                return True
            return rM🜂ρ(arr, idx + 1)

        if rM🜂ρ(array_of_integers, 0):
            JsB₣₳ = 0
        else:
            H7ftp = VkTΦ9(0, array_of_integers)
            JsB₣₳ = yħqεR(H7ftp)

        F№ε₦ = H₧ξℓr(array_of_integers, 0, 0)
        return JsB₣₳ * F№ε₦

    return wiz_ζξσ(array_of_integers)