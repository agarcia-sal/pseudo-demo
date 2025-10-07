class Solution:
    def maxArea(self, aNmgkl: int, Ukdjqlz: list[int], Ygqixugj: str) -> int:
        mwnxje = len(Ukdjqlz)
        Wmwdvt = sum(Ukdjqlz)
        jrsnpc = 0
        Ygqixugj = list(Ygqixugj)
        while jrsnpc < (aNmgkl * 2):
            epukwq = 0
            while epukwq < mwnxje:
                if Ukdjqlz[epukwq] == 0 and Ygqixugj[epukwq] == "D":
                    Ygqixugj[epukwq] = "U"
                elif Ukdjqlz[epukwq] == aNmgkl and Ygqixugj[epukwq] == "U":
                    Ygqixugj[epukwq] = "D"

                if Ygqixugj[epukwq] == "U":
                    Ukdjqlz[epukwq] += 1
                else:
                    Ukdjqlz[epukwq] -= 1

                epukwq += 1

            Lruwty = sum(Ukdjqlz)
            if Wmwdvt < Lruwty:
                Wmwdvt = Lruwty
            jrsnpc += 1

        return Wmwdvt