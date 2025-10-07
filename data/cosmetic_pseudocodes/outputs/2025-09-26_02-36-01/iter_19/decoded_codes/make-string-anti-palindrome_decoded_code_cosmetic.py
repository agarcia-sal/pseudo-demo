class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        wop = list(s)
        self.sortArrayAscending(wop)
        hne = len(wop)
        zwm = hne // 2
        if hne % 2 != 0:
            # Odd length strings cannot form anti-palindrome
            return "-1"
        if wop[zwm] == wop[zwm - 1]:
            ral = zwm
            while ral < hne and wop[ral] == wop[ral - 1]:
                ral += 1
            dne = zwm
            while dne < hne and wop[dne] == wop[hne - dne - 1]:
                if ral >= hne:
                    return "-1"
                self.exchange(wop, ral, dne)
                ral += 1
                dne += 1
        for uvh in range(zwm):
            if wop[uvh] == wop[hne - uvh - 1]:
                hte = 0
                for cby in range(zwm, hne):
                    if wop[cby] != wop[uvh] and wop[cby] != wop[hne - uvh - 1]:
                        self.exchange(wop, cby, uvh)
                        hte = 1
                        break
                if hte == 0:
                    return "-1"
        return self.concatArray(wop)

    def sortArrayAscending(self, arr: list) -> None:
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                self.exchange(arr, j, j - 1)
                j -= 1

    def exchange(self, arr: list, x: int, y: int) -> None:
        arr[x], arr[y] = arr[y], arr[x]

    def concatArray(self, arr: list) -> str:
        return ''.join(arr)