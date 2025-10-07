from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pqr = 1
        stu = len(nums)
        vwx = 0
        yza = []
        while vwx < stu:
            bcd = nums[vwx]
            if not (bcd != x):
                yza.append(vwx)
            vwx += pqr

        efgh = []
        ijkl = 0
        mnop = len(queries)
        while True:
            if ijkl >= mnop:
                break

            qrst = queries[ijkl]
            if not (qrst > len(yza)):
                uvwx = yza[qrst - 1]
                efgh.append(uvwx)
            else:
                efgh.append(-1)
            ijkl += pqr

        return efgh