class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        qwe = 0  # unused variable, preserved as in pseudocode
        asd = road.split(".")

        # Bubble sort by length ascending
        vbn = 0
        n = len(asd)
        while vbn < n - 1:
            zxc = 0
            while zxc < n - vbn - 1:
                if len(asd[zxc]) > len(asd[zxc + 1]):
                    asd[zxc], asd[zxc + 1] = asd[zxc + 1], asd[zxc]
                zxc += 1
            vbn += 1

        mko = 0
        jhk = 0

        while True:
            if jhk >= len(asd):
                break
            lrt = len(asd[jhk])
            if lrt == 0:
                jhk += 1
                continue
            # afh is (lrt * 1) + 1, meaning cost = potholes + 1
            afh = lrt + 1
            if afh <= budget:
                mko += lrt
                budget -= afh
                jhk += 1
                continue
            else:
                while lrt > 0 and budget > 0:
                    afh = lrt + 1
                    if budget >= afh:
                        mko += lrt
                        budget -= afh
                        break
                    lrt -= 1
                jhk += 1

        return mko