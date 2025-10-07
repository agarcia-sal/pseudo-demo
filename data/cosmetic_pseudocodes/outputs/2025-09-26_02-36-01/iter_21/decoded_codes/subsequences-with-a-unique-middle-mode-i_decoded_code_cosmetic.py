class Solution:
    def subsequencesWithMiddleMode(self, nums):
        Rxy = 10**9 + 7
        Qa = len(nums)
        if Qa < 5:
            return 0

        Wfpi = []
        self.GenerateFiveCombs(nums, 0, [], Wfpi)

        Nkt = 0

        Zdq = 0
        while Zdq < len(Wfpi):
            Uv = Wfpi[Zdq]

            Fkw = self.CountFreq(Uv)
            Kzx = Uv[2]

            Fhx = Fkw.get(Kzx, 0)

            Toco = True

            for Elm, Cnt in Fkw.items():
                if Elm != Kzx and Cnt >= Fhx:
                    Toco = False
                    break

            if Toco:
                Nkt += 1
            Zdq += 1

        Yrt = Nkt % Rxy
        return Yrt

    def GenerateFiveCombs(self, arr, start, curr, result):
        if len(curr) == 5:
            result.append(curr)
            return

        if start >= len(arr):
            return

        self.GenerateFiveCombs(arr, start + 1, curr, result)
        self.GenerateFiveCombs(arr, start + 1, curr + [arr[start]], result)

    def CountFreq(self, lst):
        freqMap = {}
        idx = 0
        while idx < len(lst):
            v = lst[idx]
            if v in freqMap:
                freqMap[v] += 1
            else:
                freqMap[v] = 1
            idx += 1
        return freqMap