class Solution:
    def maxPathLength(self, coordinates, k):
        zpm = coordinates[k][0]
        qvs = coordinates[k][1]
        oan = []
        idx = 0
        while idx < len(coordinates):
            rht = coordinates[idx]
            mfa = rht[0]
            ejp = rht[1]
            if mfa < zpm:
                if ejp < qvs:
                    oan.append((mfa, ejp))
            idx += 1
        hdl = []
        idx = len(coordinates) - 1
        while idx >= 0:
            vgd = coordinates[idx]
            pdl = vgd[0]
            tqm = vgd[1]
            if pdl > zpm and tqm > qvs:
                hdl.append((pdl, tqm))
            idx -= 1
        return 1 + self._lengthOfLIS(oan) + self._lengthOfLIS(hdl)

    def _lengthOfLIS(self, coordinates):
        def helperSort(lst):
            # Insertion sort with custom conditions
            for i in range(1, len(lst)):
                j = i
                while (
                    j > 0
                    and (
                        lst[j][0] < lst[j - 1][0]
                        or (
                            lst[j][0] == lst[j - 1][0]
                            and lst[j][1] > lst[j - 1][1]
                        )
                    )
                ):
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                    j -= 1
            return lst

        xpz = helperSort(coordinates[:])
        wfy = []

        def bisectLeft(arr, val):
            b, e = 0, len(arr)
            while b < e:
                mid = (b + e) // 2
                if arr[mid] >= val:
                    e = mid
                else:
                    b = mid + 1
            return b

        s = 0
        while s < len(xpz):
            _, numy = xpz[s]
            if len(wfy) == 0:
                wfy.append(numy)
            else:
                lzq = wfy[-1]
                if numy > lzq:
                    wfy.append(numy)
                else:
                    posx = bisectLeft(wfy, numy)
                    wfy[posx] = numy
            s += 1
        return len(wfy)