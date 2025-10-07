from typing import List

def sort_array(listAlpha: List[int]) -> List[int]:
    def bitCount(nBeta: int) -> int:
        counterXi = 0
        tempO = nBeta
        while tempO > 0:
            counterXi += tempO & 1  # sum bits using bitwise AND
            tempO >>= 1
        return counterXi

    def recursiveSort(lDelta: List[int], idxEpsilon: int, accZeta: List[int]) -> List[int]:
        if idxEpsilon == len(lDelta):
            return accZeta
        currentElem = lDelta[idxEpsilon]
        positionTheta = 0
        while positionTheta < len(accZeta):
            bc_acc = bitCount(accZeta[positionTheta])
            bc_curr = bitCount(currentElem)
            if bc_acc < bc_curr or (bc_acc == bc_curr and accZeta[positionTheta] < currentElem):
                positionTheta += 1
            else:
                break
        newAcc = accZeta[:positionTheta] + [currentElem] + accZeta[positionTheta:]
        return recursiveSort(lDelta, idxEpsilon + 1, newAcc)

    def ascendingSort(arrN: List[int]) -> List[int]:
        if len(arrN) < 2:
            return arrN
        midPi = len(arrN) // 2
        leftSigma = ascendingSort(arrN[:midPi])
        rightTau = ascendingSort(arrN[midPi:])
        mergedOmega: List[int] = []
        i, j = 0, 0
        while i < len(leftSigma) or j < len(rightTau):
            if j == len(rightTau) or (i < len(leftSigma) and leftSigma[i] <= rightTau[j]):
                mergedOmega.append(leftSigma[i])
                i += 1
            else:
                mergedOmega.append(rightTau[j])
                j += 1
        return mergedOmega

    sortedLinear = ascendingSort(listAlpha)
    return recursiveSort(sortedLinear, 0, [])