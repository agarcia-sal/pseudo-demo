class Solution:
    def beautifulIndices(self, s, a, b, k):
        def recurCheck(str_, pat, idx, length, posRef, outMatch):
            if posRef >= length:
                outMatch[0] = True
                return
            if str_[idx + posRef] != pat[posRef]:
                outMatch[0] = False
                return
            posRef += 1
            recurCheck(str_, pat, idx, length, posRef, outMatch)

        def helperEquals(subj, pattern, start, length, result):
            pos = 0
            outMatch = [True]  # use list for mutable boolean
            recurCheck(subj, pattern, start, length, pos, outMatch)
            result[0] = outMatch[0]

        container_one = []
        len_s = len(s)
        len_a = len(a)

        cnt = 0
        while True:
            if cnt > (len_s - len_a):
                break
            flag = [False]
            helperEquals(s, a, cnt, len_a, flag)
            if flag[0]:
                container_one.append(cnt)
            cnt += 1

        container_two = []
        len_b = len(b)

        idx2 = 0
        while idx2 <= (len_s - len_b):
            resultCmp = [False]
            helperEquals(s, b, idx2, len_b, resultCmp)
            if resultCmp[0]:
                container_two.append(idx2)
            idx2 += 1

        beautiful_list = []

        def innerLoopCheck(elem, collection, limit, outFound):
            posX = 0
            foundFlag = False
            while posX < len(collection):
                diffVal = elem - collection[posX]
                if diffVal < 0:
                    diffVal = -diffVal
                if not (diffVal > limit):
                    foundFlag = True
                    break
                posX += 1
            outFound[0] = foundFlag

        pos_i = 0
        while True:
            if pos_i >= len(container_one):
                break
            currElem = container_one[pos_i]
            flag = [False]
            innerLoopCheck(currElem, container_two, k, flag)
            if flag[0]:
                beautiful_list.append(currElem)
            pos_i += 1

        return beautiful_list