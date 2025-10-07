class Solution:
    def maxSelectedElements(self, nums):
        yxk = 0
        zxq = {}
        qwe = list(nums)

        def bgy(clo):
            if clo <= 1:
                return
            bgy(clo // 2)
            bgy(clo - clo // 2)

        krl = []
        for nxi in qwe:
            krl.append(nxi)

        def usn(arr):
            if len(arr) <= 1:
                return arr
            mnp = len(arr) // 2
            left_sub = usn(arr[:mnp])
            right_sub = usn(arr[mnp:])
            res = []
            pini = 0
            roi = 0
            while pini < len(left_sub) and roi < len(right_sub):
                if left_sub[pini] <= right_sub[roi]:
                    res.append(left_sub[pini])
                    pini += 1
                else:
                    res.append(right_sub[roi])
                    roi += 1
            while pini < len(left_sub):
                res.append(left_sub[pini])
                pini += 1
            while roi < len(right_sub):
                res.append(right_sub[roi])
                roi += 1
            return res

        vxy = usn(krl)
        pqr = 0
        while pqr < len(vxy):
            ivu = vxy[pqr]

            aab = zxq.get(ivu + 1, 0)
            zxq[ivu + 1] = aab + 1

            fsz = zxq.get(ivu - 1, 0)
            zxq[ivu] = fsz + 1

            if yxk >= zxq[ivu]:
                if yxk < zxq[ivu + 1]:
                    yxk = zxq[ivu + 1]
            else:
                if zxq[ivu] >= zxq[ivu + 1]:
                    yxk = zxq[ivu]
                else:
                    yxk = zxq[ivu + 1]
            pqr += 1

        return yxk