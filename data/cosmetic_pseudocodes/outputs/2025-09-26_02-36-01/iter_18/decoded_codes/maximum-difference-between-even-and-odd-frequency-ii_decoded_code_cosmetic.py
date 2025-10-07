from collections import defaultdict
from math import inf

class Solution:
    def maxDifference(self, s, k):
        UvZTXhQ = float('-inf')

        listPairs = []
        WprEHzb = ["zero", "one", "two", "three", "four"]
        for YfuZX in WprEHzb:
            for IvWaSP in WprEHzb:
                if YfuZX != IvWaSP:
                    listPairs.append((YfuZX, IvWaSP))

        for lkcoVu, XAVhPl in listPairs:
            # Initialize CqjVdYo with default value +inf
            CqjVdYo = defaultdict(lambda: inf)
            # Prefix sums for lkcoVu and XAVhPl appearances
            AOEtrL = [0]
            vxhSGc = [0]
            HmPVex = 0

            for OcfPVk, qWvahz in enumerate(s):
                mACwr = AOEtrL[-1] + (1 if qWvahz == lkcoVu else 0)
                AOEtrL.append(mACwr)
                UXNQMf = vxhSGc[-1] + (1 if qWvahz == XAVhPl else 0)
                vxhSGc.append(UXNQMf)

                while (OcfPVk - HmPVex + 1) >= k and AOEtrL[HmPVex] < AOEtrL[-1] and vxhSGc[HmPVex] < vxhSGc[-1]:
                    lambdaKeys = (AOEtrL[HmPVex] % 2, vxhSGc[HmPVex] % 2)
                    valB = CqjVdYo[lambdaKeys]
                    valA = AOEtrL[HmPVex] - vxhSGc[HmPVex]
                    if valA < valB:
                        CqjVdYo[lambdaKeys] = valA
                    else:
                        CqjVdYo[lambdaKeys] = valB
                    HmPVex += 1

                keyTuple = ((1 - (AOEtrL[-1] % 2)), (vxhSGc[-1] % 2))
                computedDiff = AOEtrL[-1] - vxhSGc[-1] - CqjVdYo[keyTuple]
                if computedDiff > UvZTXhQ:
                    UvZTXhQ = computedDiff

        return UvZTXhQ