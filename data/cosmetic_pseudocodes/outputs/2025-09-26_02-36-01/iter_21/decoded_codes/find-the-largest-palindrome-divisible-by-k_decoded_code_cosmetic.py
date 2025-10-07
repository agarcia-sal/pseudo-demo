class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        z1 = 1
        if n == z1:
            z2 = 9
            while z2 >= z1:
                z3 = z2 % k
                if z3 == 0:
                    return str(z2)
                z2 -= z1
            return "0"

        z4 = (n + z1) // 2
        z7 = "9" * z4
        z8 = int(z7)
        while z8 > 0:
            z9 = n % 2
            if z9 == 0:
                z5 = str(z8)
                z6 = z5[::-1]
                z10 = z5 + z6
                z11 = int(z10)
            else:
                z5 = str(z8)
                z12 = z5[:-1]
                z6 = z12[::-1]
                z10 = z5 + z6
                z11 = int(z10)
            z13 = z11 % k
            if z13 == 0:
                return str(z11)
            z8 -= 1
        return "0"