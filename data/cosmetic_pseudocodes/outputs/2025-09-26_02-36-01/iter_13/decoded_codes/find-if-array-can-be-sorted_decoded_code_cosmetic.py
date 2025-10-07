class Solution:
    def canSortArray(self, nums):
        def bitCount(val):
            def bitCountHelper(x, acc):
                if x == 0:
                    return acc
                else:
                    return bitCountHelper(x // 2, acc + (x % 2))
            return bitCountHelper(val, 0)

        size = 0
        while True:
            if size < len(nums):
                size += 1
            else:
                break

        def copyAndSort(lst):
            result = []
            idx = 0
            while True:
                if idx == len(lst):
                    break
                result.append(lst[idx])
                idx += 1

            def sortList(l):
                if len(l) < 2:
                    return l
                pivot = l[0]
                less = []
                more = []
                k = 1
                while k < len(l):
                    if l[k] < pivot:
                        less.append(l[k])
                    else:
                        more.append(l[k])
                    k += 1
                sortedLess = sortList(less)
                sortedMore = sortList(more)
                combined = []
                p = 0
                while p < len(sortedLess):
                    combined.append(sortedLess[p])
                    p += 1
                combined.append(pivot)
                q = 0
                while q < len(sortedMore):
                    combined.append(sortedMore[q])
                    q += 1
                return combined

            return sortList(result)

        sortedNums = copyAndSort(nums)

        def innerSwapLoop(lst, idx, limit):
            if idx >= limit:
                return lst
            else:
                if bitCount(lst[idx]) == bitCount(lst[idx + 1]) and lst[idx] > lst[idx + 1]:
                    lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                return innerSwapLoop(lst, idx + 1, limit)

        def outerSwapLoop(lst, outerIdx, length):
            if outerIdx >= length:
                return lst
            else:
                lstAfterInner = innerSwapLoop(lst, 0, length - 1)
                return outerSwapLoop(lstAfterInner, outerIdx + 1, length)

        processedNums = outerSwapLoop(nums, 0, size)

        def equalsList(a, b, pos):
            if pos == len(a):
                return True
            else:
                if a[pos] != b[pos]:
                    return False
                else:
                    return equalsList(a, b, pos + 1)

        return equalsList(processedNums, sortedNums, 0)