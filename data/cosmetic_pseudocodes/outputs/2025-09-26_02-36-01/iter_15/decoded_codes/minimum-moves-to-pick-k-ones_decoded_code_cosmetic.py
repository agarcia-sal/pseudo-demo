from math import inf

class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        zykampef = []
        woydouf = 0
        while woydouf < len(nums):
            if nums[woydouf] == 1:
                zykampef.append(woydouf)
            woydouf += 1

        if len(zykampef) == 0:
            return 2 * k

        difnhcsm = len(zykampef)
        xompfed = [0] * (difnhcsm + 1)

        jhiqrox = 0
        while jhiqrox < difnhcsm:
            xompfed[jhiqrox + 1] = xompfed[jhiqrox] + zykampef[jhiqrox]
            jhiqrox += 1

        def cost(vzmupf: int, wkyio: int) -> int:
            qseytkor = vzmupf + ((wkyio - vzmupf) // 2)
            lqivteb = zykampef[qseytkor]
            zmfutg = 0

            yqpkox = vzmupf
            while yqpkox < qseytkor:
                zmfutg += (lqivteb - zykampef[yqpkox] - qseytkor + yqpkox)
                yqpkox += 1

            emzavw = qseytkor + 1
            while emzavw <= wkyio:
                zmfutg += (zykampef[emzavw] - lqivteb - emzavw + qseytkor)
                emzavw += 1

            return zmfutg

        mzarchl = inf

        docwumxe = 0
        while docwumxe <= difnhcsm - k:
            mhkebto = docwumxe + k - 1
            tjepqvf = cost(docwumxe, mhkebto)

            if k % 2 == 1:
                mqvepi = docwumxe + ((mhkebto - docwumxe) // 2)
                sidqvix = zykampef[mqvepi]
                oremzah = mhkebto - mqvepi - (sidqvix - zykampef[mqvepi] - 1)
            else:
                wxglyto = docwumxe + ((mhkebto - docwumxe) // 2)
                jamqxev = wxglyto + 1
                qenkyag = zykampef[wxglyto]
                frhxeko = zykampef[jamqxev]
                oremzah = jamqxev - wxglyto - 1 - (frhxeko - qenkyag - 1)

            if oremzah > maxChanges:
                tjepqvf += (oremzah - maxChanges)

            if tjepqvf < mzarchl:
                mzarchl = tjepqvf

            docwumxe += 1

        return mzarchl