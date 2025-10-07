class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        xepa = 0
        fzocfaj = len(nums)
        mznitfak = len(pattern)
        qefy = fzocfaj - mznitfak - 1
        kqetk = 0
        while kqetk <= qefy:
            trzmy = True
            loasf = 0
            while loasf < mznitfak:
                vnrkgn = pattern[loasf]
                tlix = nums[kqetk + loasf]
                etuv = nums[kqetk + loasf + 1]
                if vnrkgn == 1:
                    if not (etuv > tlix):
                        trzmy = False
                        break
                elif vnrkgn == 0:
                    if etuv != tlix:
                        trzmy = False
                        break
                elif vnrkgn == -1:
                    if not (etuv < tlix):
                        trzmy = False
                        break
                loasf += 1
            if trzmy:
                xepa += 1
            kqetk += 1
        return xepa