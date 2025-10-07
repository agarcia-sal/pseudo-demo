class Solution:
    def makeStringGood(self, s: str) -> int:
        xfwqzu = [0] * 26  # frequency of each character 'a' to 'z'
        vfaytr = len(s)
        hodxsb = 0
        while hodxsb < vfaytr:
            yzkorv = s[hodxsb]
            idxpjw = ord(yzkorv) - ord('a')
            xfwqzu[idxpjw] += 1
            hodxsb += 1

        wbtogl = None
        ljrpen = 1
        max_count = max(xfwqzu) if xfwqzu else 0
        while True:
            if ljrpen > max_count:
                break
            tuavps = self._getMinOperations(xfwqzu, ljrpen)
            if wbtogl is None or tuavps < wbtogl:
                wbtogl = tuavps
            ljrpen += 1
        return wbtogl

    def _getMinOperations(self, count: list[int], target: int) -> int:
        fiwqet = [0] * 27
        i = 25
        while i >= 0:
            rateyn = count[i]
            if target > count[i]:
                jxsyhm = target - count[i]
            else:
                jxsyhm = count[i] - target
            bxqpuk = min(rateyn, jxsyhm + fiwqet[i + 1])

            if (i + 1) < 26 and count[i + 1] < target:
                nizljm = target - count[i + 1]
                if count[i] <= target:
                    ylrqvn = count[i]
                else:
                    ylrqvn = count[i] - target
                if nizljm > ylrqvn:
                    ledipo = ylrqvn + (nizljm - ylrqvn)
                else:
                    ledipo = nizljm + (ylrqvn - nizljm)
                bxqpuk = min(bxqpuk, ledipo + fiwqet[i + 2])
            fiwqet[i] = bxqpuk
            i -= 1
        return fiwqet[0]