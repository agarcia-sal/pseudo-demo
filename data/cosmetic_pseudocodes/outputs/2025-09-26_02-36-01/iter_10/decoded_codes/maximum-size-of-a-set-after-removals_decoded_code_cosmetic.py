from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        def lengthOfList(xs: List[int]) -> int:
            def helper(i: int) -> int:
                if i == len(xs):
                    return 0
                else:
                    return 1 + helper(i + 1)
            return helper(0)

        def length(xs: List[int]) -> int:
            return lengthOfList(xs)

        def uniqueElements(xs: List[int]) -> List[int]:
            def contains(lst: List[int], val: int) -> bool:
                def process(i: int) -> bool:
                    if i == length(lst):
                        return False
                    else:
                        if lst[i] == val:
                            return True
                        else:
                            return process(i + 1)
                return process(0)

            def collect(i: int, acc: List[int]) -> List[int]:
                if i == length(xs):
                    return acc
                else:
                    if contains(acc, xs[i]):
                        return collect(i + 1, acc)
                    else:
                        return collect(i + 1, acc + [xs[i]])
            return collect(0, [])

        def intersection(xs: List[int], ys: List[int]) -> List[int]:
            def contains(lst: List[int], val: int) -> bool:
                def loop(j: int) -> bool:
                    if j == length(lst):
                        return False
                    else:
                        if lst[j] == val:
                            return True
                        else:
                            return loop(j + 1)
                return loop(0)

            def build(i: int, acc: List[int]) -> List[int]:
                if i == length(xs):
                    return acc
                else:
                    if contains(ys, xs[i]):
                        return build(i + 1, acc + [xs[i]])
                    else:
                        return build(i + 1, acc)
            return build(0, [])

        def difference(xs: List[int], ys: List[int]) -> List[int]:
            def contains(lst: List[int], val: int) -> bool:
                def rec(k: int) -> bool:
                    if k == length(lst):
                        return False
                    else:
                        if lst[k] == val:
                            return True
                        else:
                            return rec(k + 1)
                return rec(0)

            def gather(i: int, acc: List[int]) -> List[int]:
                if i == length(xs):
                    return acc
                else:
                    if contains(ys, xs[i]):
                        return gather(i + 1, acc)
                    else:
                        return gather(i + 1, acc + [xs[i]])
            return gather(0, [])

        def minVal(a: int, b: int) -> int:
            return a if a < b else b

        def maxVal(a: int, b: int) -> int:
            return a if a > b else b

        def halfDivide(x: int) -> int:
            return x // 2

        c = length(nums1)
        d = halfDivide(c)

        e = uniqueElements(nums1)
        f = uniqueElements(nums2)

        g = intersection(e, f)

        h = difference(e, g)
        i = difference(f, g)

        j = minVal(d, length(h))
        k = minVal(d, length(i))

        l = maxVal(0, d - j) + maxVal(0, d - k)

        m = j + k + minVal(l, length(g))

        return m