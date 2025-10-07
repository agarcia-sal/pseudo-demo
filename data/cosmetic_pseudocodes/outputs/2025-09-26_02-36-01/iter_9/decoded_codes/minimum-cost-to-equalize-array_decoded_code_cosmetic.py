class Solution:
    def minCostToEqualizeArray(self, lambdaOmega, cost1, cost2):
        omegaTheta = 1_000_000_007
        PsiPi = len(lambdaOmega)
        alphaBeta = lambdaOmega[0]
        tauSigma = lambdaOmega[0]
        NuXi = 0

        kappaRho = 0
        while kappaRho < PsiPi:
            chiPsi = lambdaOmega[kappaRho]
            if chiPsi < alphaBeta:
                alphaBeta = chiPsi
            if chiPsi > tauSigma:
                tauSigma = chiPsi
            NuXi += chiPsi
            kappaRho += 1

        if (cost1 * 2) <= cost2 or PsiPi < 3:
            deltaSigma = (tauSigma * PsiPi) - NuXi
            return (cost1 * deltaSigma) % omegaTheta

        def zetaEta(kappaOmega):
            epsilonDelta = kappaOmega - alphaBeta
            phiChi = (kappaOmega * PsiPi) - NuXi
            upsilonLambda = min(phiChi // 2, phiChi - epsilonDelta)
            return cost1 * (phiChi - 2 * upsilonLambda) + cost2 * upsilonLambda

        def etaKappa():
            iotaGamma = tauSigma
            lambdaBeta = 2 * tauSigma - 1
            rhoSigma = None

            def recursiveSearch(x):
                nonlocal rhoSigma
                if x > lambdaBeta:
                    return rhoSigma
                psiAlpha = zetaEta(x)
                if rhoSigma is None or psiAlpha < rhoSigma:
                    rhoSigma = psiAlpha
                return recursiveSearch(x + 1)

            return recursiveSearch(iotaGamma)

        omegaPhi = etaKappa()
        return omegaPhi % omegaTheta