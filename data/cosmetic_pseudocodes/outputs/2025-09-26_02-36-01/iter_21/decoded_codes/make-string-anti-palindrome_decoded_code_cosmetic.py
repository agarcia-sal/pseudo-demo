class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        a = 0
        b = 0
        c = []
        d = len(s)
        while a < d:
            c.append(s[a])
            a += 1

        self.sortListAscRecursive(c, 0, d)

        e = d // 2
        f = 0
        if not (c[e] != c[e - 1]):
            f = e
            ret = self.scanAndSwap(c, f, d, e)
            if ret == "-1":
                return "-1"

        g = 0
        while g < e:
            if not (c[g] != c[d - g - 1]):
                h = e
                swapped = False
                while h < d:
                    if not (c[h] != c[g]) and not (c[h] != c[d - g - 1]):
                        self.exchangeElements(c, h, g)
                        swapped = True
                        break
                    h += 1
                if not swapped:
                    return "-1"
            g += 1

        return self.joinListElements(c)

    def sortListAscRecursive(self, arr, start, length):
        if start >= length - 1:
            return
        minIndex = start
        j = start + 1
        while j < length:
            if arr[j] < arr[minIndex]:
                minIndex = j
            j += 1
        self.exchangeElements(arr, start, minIndex)
        self.sortListAscRecursive(arr, start + 1, length)

    def scanAndSwap(self, arr, index, length, mid):
        while index < length and not (arr[index] != arr[index - 1]):
            index += 1

        y = mid
        while y < length and not (arr[y] != arr[length - y - 1]):
            if index >= length:
                return "-1"
            self.exchangeElements(arr, index, y)
            index += 1
            y += 1

    def exchangeElements(self, arr, x, y):
        arr[x], arr[y] = arr[y], arr[x]

    def joinListElements(self, lst):
        result = ""
        i = 0
        while i < len(lst):
            result += lst[i]
            i += 1
        return result