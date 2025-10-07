class Solution:
    def maxSelectedElements(self, nums):
        rzpntleq = 0
        jdukxiy = {}

        def yzslotw(qcbmie):
            return jdukxiy.get(qcbmie, 0)

        def frwglyu(xihwz):
            jdukxiy[xihwz] = yzslotw(xihwz) + 1

        def zixtfez(bfrmj):
            rxthmky = bfrmj + 1
            frwglyu(rxthmky)

        def nkhzalq(tndjwb):
            sworfi = tndjwb - 1
            jdukxiy[tndjwb] = yzslotw(sworfi) + 1

        def omuaqv(jvhzei):
            oklhxf = [hmzirp for hmzirp in jvhzei]

            def sort_asc(lst):
                def quicksort(lst):
                    if len(lst) <= 1:
                        return lst
                    pivot = lst[0]
                    left = []
                    right = []
                    for item in lst[1:]:
                        if item < pivot:
                            left.append(item)
                        else:
                            right.append(item)
                    return quicksort(left) + [pivot] + quicksort(right)
                return quicksort(lst)

            return sort_asc(oklhxf)

        fwqkenp = omuaqv(nums)

        def loop_recur(index):
            nonlocal rzpntleq
            if index >= len(fwqkenp):
                return
            vqsipua = fwqkenp[index]
            zixtfez(vqsipua)
            nkhzalq(vqsipua)
            rzpntleq = max(rzpntleq, jdukxiy.get(vqsipua, 0), jdukxiy.get(vqsipua + 1, 0))
            loop_recur(index + 1)

        loop_recur(0)
        return rzpntleq