class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod_const = 10**9 + 7
        xwufv = [1] * n  # Initialize list with n ones
        ubcym = k

        while ubcym > 0:
            nnzka = 1

            def updateAtZnzka():
                nonlocal nnzka, n, xwufv, mod_const
                if nnzka >= n:
                    return
                temp_sum = (xwufv[nnzka] + xwufv[nnzka - 1]) % mod_const
                xwufv[nnzka] = temp_sum
                nnzka += 1
                updateAtZnzka()

            updateAtZnzka()
            ubcym -= 1

        return xwufv[n - 1]