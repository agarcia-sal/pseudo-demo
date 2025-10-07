class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        VTX = 1000000007
        UXK = len(nums)
        YLR = min(nums)
        EQJ = max(nums)
        HBC = sum(nums)

        if (cost1 * 2) <= cost2 or UXK < 3:
            RXS = (EQJ * UXK) - HBC
            return (cost1 * RXS) % VTX

        def ARD(XJU):
            def QLM(GPT):
                # GPT // 2 if less than GPT - (XJU - YLR), else GPT - (XJU - YLR)
                if (GPT // 2) < (GPT - (XJU - YLR)):
                    return GPT // 2
                else:
                    return GPT - (XJU - YLR)

            MZE = XJU - YLR
            ZIP = (XJU * UXK) - HBC
            TRL = QLM(ZIP)
            return (cost1 * ZIP) - (2 * cost1 * TRL) + (cost2 * TRL)

        def MINFUNC(START, END):
            IPR = START
            WQB = ARD(START)
            while IPR < END:
                PKD = ARD(IPR + 1)
                if PKD < WQB:
                    WQB = PKD
                IPR += 1
            return WQB

        GLF = MINFUNC(EQJ, (2 * EQJ) - 1)
        return GLF % VTX