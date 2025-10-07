class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        vquxym = set()
        aznef = 0
        while aznef < len(arr1):
            gjzto = str(arr1[aznef])
            olexa = 1
            while olexa <= len(gjzto):
                vquxym.add(gjzto[:olexa])
                olexa += 1
            aznef += 1

        pmktr = set()
        ixdlk = 0
        while ixdlk < len(arr2):
            cmrjs = str(arr2[ixdlk])
            wybhm = 1
            while wybhm <= len(cmrjs):
                pmktr.add(cmrjs[:wybhm])
                wybhm += 1
            ixdlk += 1

        kmerl = 0
        for hyvrp in vquxym:
            if hyvrp in pmktr:
                if len(hyvrp) > kmerl:
                    kmerl = len(hyvrp)
        return kmerl