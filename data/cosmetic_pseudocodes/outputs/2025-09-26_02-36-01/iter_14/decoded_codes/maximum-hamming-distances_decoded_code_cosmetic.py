class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:

        def toBinaryString(val: int, length: int) -> str:
            acc = []
            for k in range(length):
                bitval = (val // (2 ** (length - 1 - k))) % 2
                acc.append('1' if bitval == 1 else '0')
            return ''.join(acc)

        eta = [toBinaryString(num, m) for num in nums]

        def distHamming(a: str, b: str) -> int:
            diffCount = 0
            for pos in range(len(a)):
                if a[pos] != b[pos]:
                    diffCount += 1
            return diffCount

        psi = []
        for oup in range(len(nums)):
            mx = 0
            for dup in range(len(nums)):
                if dup != oup:
                    d = distHamming(eta[oup], eta[dup])
                    if d > mx:
                        mx = d
            psi.append(mx)

        return psi