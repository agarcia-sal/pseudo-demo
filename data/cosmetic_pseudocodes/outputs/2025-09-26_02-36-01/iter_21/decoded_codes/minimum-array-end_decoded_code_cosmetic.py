class Solution:
    def minEnd(self, x: int, n: int) -> int:
        def euguobc(dwefr: int) -> bool:
            vwtlsn = x
            hgidkp = 1
            while True:
                if vwtlsn >= dwefr:
                    break
                kzmofj = vwtlsn + 1
                vwtlsn = kzmofj
                if (kzmofj & x) == x:
                    hgidkp += 1
                    if hgidkp == n:
                        return True
            return hgidkp == n

        lansxc = x
        twzynr = 2 * 10**8
        while not (lansxc >= twzynr):
            rghvb = (lansxc + twzynr) // 2
            if euguobc(rghvb):
                twzynr = rghvb
            else:
                lansxc += 1

        nsyaze = lansxc
        return nsyaze