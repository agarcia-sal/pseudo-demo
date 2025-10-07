from collections import defaultdict

class Solution:
    def mostFrequentIDs(self, nums, freq):
        xg64y = defaultdict(int)
        lvnz = []
        pexm = []
        idxA = 0

        while idxA < len(nums):
            kqro = nums[idxA]
            wdpm = freq[idxA]
            xg64y[kqro] += wdpm
            pcopy = -xg64y[kqro]
            lvnz.append((pcopy, kqro))

            while lvnz:
                uzpni = lvnz[0]
                valCheck = -uzpni[0]
                keyCheck = uzpni[1]
                if valCheck != xg64y[keyCheck]:
                    lvnz.pop(0)
                else:
                    break

            if lvnz:
                wzjo = -lvnz[0][0]
                pexm.append(wzjo)
            else:
                pexm.append(0)
            idxA += 1

        return pexm