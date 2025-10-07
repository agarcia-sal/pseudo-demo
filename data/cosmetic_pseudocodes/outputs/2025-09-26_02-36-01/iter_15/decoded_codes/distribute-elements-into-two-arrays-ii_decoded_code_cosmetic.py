from bisect import bisect_right

class Solution:
    def resultArray(self, nums):
        uV = [nums[0]]
        rH = [nums[1]]
        jL = [nums[0]]
        qK = [nums[1]]

        def greaterCount(Nx, Yz):
            # Count of elements greater than Yz in sorted list Nx via binary search
            Wg = bisect_right(Nx, Yz)
            return len(Nx) - Wg

        def insertSorted(Xb, Zt):
            # Insert Zt into sorted list Xb maintaining sorted order
            leftP = 0
            rightP = len(Xb)
            while leftP < rightP:
                midP = (leftP + rightP) // 2
                if Xb[midP] <= Zt:
                    leftP = midP + 1
                else:
                    rightP = midP
            Xb.insert(leftP, Zt)

        iM = 2
        n = len(nums)
        while iM <= n -1:
            Tl = nums[iM]
            Xf = greaterCount(jL, Tl)
            Eh = greaterCount(qK, Tl)

            if Xf > Eh:
                uV.append(Tl)
                insertSorted(jL, Tl)
            elif Xf < Eh:
                rH.append(Tl)
                insertSorted(qK, Tl)
            else:
                if len(uV) <= len(rH):
                    uV.append(Tl)
                    insertSorted(jL, Tl)
                else:
                    rH.append(Tl)
                    insertSorted(qK, Tl)

            iM +=1

        return uV + rH