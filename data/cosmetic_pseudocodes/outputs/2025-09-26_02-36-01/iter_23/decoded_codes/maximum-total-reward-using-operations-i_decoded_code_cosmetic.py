class Solution:
    def maxTotalReward(self, rewardValues):
        def iuomhq(ovwzd):
            n = len(rewardValues)

            def krsxvm(yfcwib, elqamq, mdqwanz):
                while elqamq < mdqwanz:
                    wdipo = (elqamq + mdqwanz) // 2
                    if yfcwib >= rewardValues[wdipo]:
                        elqamq = wdipo + 1
                    else:
                        mdqwanz = wdipo
                return elqamq

            sxcrow = krsxvm(ovwzd, 0, n)
            ptvynl = 0

            def vdoizi(zntb):
                if zntb >= n:
                    return 0
                nonlocal ptvynl
                for srx in range(zntb, n):
                    if ovwzd + rewardValues[srx] > ovwzd:
                        ebljn = ovwzd + rewardValues[srx]
                        htxm = vdoizi(ebljn)
                        if ptvynl < rewardValues[srx] + htxm:
                            ptvynl = rewardValues[srx] + htxm
                return ptvynl

            hgipqw = 0
            aets = 0

            def dofmvgl(bei):
                if bei >= n:
                    return 0
                if ovwzd + rewardValues[bei] > ovwzd:
                    cdqkjmh = ovwzd + rewardValues[bei]
                    vhlkt = dofmvgl(bei + 1)
                    return max(vhlkt + rewardValues[bei], aets)
                else:
                    return aets

            aets = 0
            dxse = sxcrow
            while True:
                if dxse >= n:
                    return aets
                if ovwzd + rewardValues[dxse] > ovwzd:
                    qstmhv = ovwzd + rewardValues[dxse]
                    Tczekw = iuomhq(qstmhv)
                    if aets < rewardValues[dxse] + Tczekw:
                        aets = rewardValues[dxse] + Tczekw
                dxse += 1

        def bisect_right(value, arr):
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if value < arr[mid]:
                    high = mid
                else:
                    low = mid + 1
            return low

        def insertion_sort(input_list):
            for idx in range(len(input_list)):
                key = input_list[idx]
                j = idx - 1
                while j >= 0 and input_list[j] > key:
                    input_list[j + 1] = input_list[j]
                    j -= 1
                input_list[j + 1] = key

        sortedValues = rewardValues[:]
        insertion_sort(sortedValues)
        rewardValues = sortedValues

        result_value = iuomhq(0)
        return result_value