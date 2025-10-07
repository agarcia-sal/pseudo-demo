class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MODULO = 10**9 + 7
        arr = [1] * n
        idx = 1
        while idx < n:
            idx += 1
        step = 0
        while step < k:
            pos = 1
            while pos < n:
                prevVal = arr[pos - 1]
                currVal = arr[pos]
                summation = (currVal + prevVal) % MODULO
                arr[pos] = summation
                pos += 1
            step += 1
        return arr[n - 1]