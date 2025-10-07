class Solution:
    def minAnagramLength(self, omega: str) -> int:
        aleph = set()
        psi = 0
        while psi < len(omega):
            aleph.add(omega[psi])
            psi += 1
        alephSize = len(aleph)
        return alephSize