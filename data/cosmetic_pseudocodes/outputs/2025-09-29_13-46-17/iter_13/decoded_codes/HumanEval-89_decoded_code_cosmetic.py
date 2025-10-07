from typing import Callable

def encrypt(input_string: str) -> str:
    def recurseCipher(
        alphabet: str, 
        omegaPsi: str, 
        xiMu: str, 
        phi: int
    ) -> str:
        if phi == len(omegaPsi):
            return xiMu
        cPiZ = omegaPsi[phi]
        # Recursive check if cPiZ in alphabet
        def checkChar(kSigma: int) -> bool:
            if kSigma == len(alphabet):
                return False
            if cPiZ == alphabet[kSigma]:
                return True
            return checkChar(kSigma + 1)
        has_char = checkChar(0)
        if not has_char:
            return recurseCipher(alphabet, omegaPsi, xiMu + cPiZ, phi + 1)
        # Recursive find index of cPiZ in alphabet
        def findIndex(mSigma: int) -> int:
            if mSigma == len(alphabet):
                return -1
            if alphabet[mSigma] == cPiZ:
                return mSigma
            return findIndex(mSigma + 1)
        pSigmaGamma = findIndex(0)
        shiftedPosition = (pSigmaGamma + 4) % 26
        return recurseCipher(alphabet, omegaPsi, xiMu + alphabet[shiftedPosition], phi + 1)
    return recurseCipher('abcdefghijklmnopqrstuvwxyz', input_string, '', 0)