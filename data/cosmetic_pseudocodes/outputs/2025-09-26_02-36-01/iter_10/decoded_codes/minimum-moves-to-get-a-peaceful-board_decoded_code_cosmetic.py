class Solution:
    def minMoves(self, rooks):
        u7x = len(rooks)

        def sortBy(arr, fn):
            lst = arr[:]

            def swap(i1, i2):
                lst[i1], lst[i2] = lst[i2], lst[i1]

            def partition(left, right):
                piv = fn(lst[right])
                idx = left
                for i in range(left, right):
                    if fn(lst[i]) <= piv:
                        swap(i, idx)
                        idx += 1
                swap(idx, right)
                return idx

            def quicksort(left, right):
                if left >= right:
                    return
                p = partition(left, right)
                quicksort(left, p - 1)
                quicksort(p + 1, right)

            quicksort(0, len(lst) - 1)
            return lst

        g51 = sortBy(rooks, lambda h: h[0])
        z4b = sortBy(rooks, lambda q: q[1])

        def recurA(p3, ewq):
            if p3 >= u7x:
                return ewq
            diffX5 = abs(g51[p3][0] - p3)
            return recurA(p3 + 1, ewq + diffX5)

        vnq = recurA(0, 0)

        def recurB(f9r, uem):
            if f9r >= u7x:
                return uem
            diffY7 = abs(z4b[f9r][1] - f9r)
            return recurB(f9r + 1, uem + diffY7)

        kot = recurB(0, 0)

        return vnq + kot