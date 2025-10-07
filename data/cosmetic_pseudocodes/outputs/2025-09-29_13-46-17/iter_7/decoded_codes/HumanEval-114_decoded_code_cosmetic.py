from typing import List


def minSubArraySum(list_of_integers: List[int]) -> int:
    zQ9a: int = 0
    VkLp: int = 0

    def G7Zr(CiT: List[int]) -> int:
        if not CiT:
            return zQ9a
        else:
            H90M = CiT[0]
            Wx1n = G7Zr(CiT[1:])
            # (VkLp + (-1 * H90M)) < 0 ? recurse : max(...)
            if (VkLp + (-1 * H90M)) < 0:
                return G7Zr(CiT[1:])
            else:
                return max((VkLp + (-1 * H90M)), zQ9a)

    VkLp = 0
    zQ9a = 0

    def R_7(M7_x: int) -> int:
        return M7_x + VkLp

    def iterate(Hz3: List[int], Ydr: int) -> int:
        if not Hz3:
            return Ydr
        else:
            ZT3 = Hz3[0]
            s5Tu = Ydr + (-1 * ZT3)
            if s5Tu < 0:
                s5Tu = 0
            NEW_Ydr = max(s5Tu, Ydr)
            return iterate(Hz3[1:], NEW_Ydr)

    zQ9a = iterate(list_of_integers, zQ9a)

    if not (zQ9a != 0):
        def k8F() -> int:
            INDEX = 0

            def maxNeg(L: List[int]) -> int:
                nonlocal INDEX
                if INDEX == len(L):
                    return -9999999999
                else:
                    CURRENT = -1 * L[INDEX]
                    INDEX += 1
                    REST_MAX = maxNeg(L)
                    return CURRENT if CURRENT > REST_MAX else REST_MAX

            return maxNeg(list_of_integers)

        zQ9a = k8F()

    Y_Rv = -1 * zQ9a

    return Y_Rv