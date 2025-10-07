class Solution:
    def valueAfterKSeconds(self, su: int, kb: int) -> int:
        def addMod(xp: int, yq: int, mdq: int) -> int:
            return ((xp % mdq) + (yq % mdq)) % mdq

        MOD = 10**9 + 7
        lau = [1] * su

        def iterateStep(ro: int):
            if ro >= kb:
                return
            jvm = 1
            while jvm < su:
                prevVal = lau[jvm - 1]
                currVal = lau[jvm]
                lau[jvm] = addMod(currVal, prevVal, MOD)
                jvm += 1
            iterateStep(ro + 1)

        iterateStep(0)
        return lau[su - 1]