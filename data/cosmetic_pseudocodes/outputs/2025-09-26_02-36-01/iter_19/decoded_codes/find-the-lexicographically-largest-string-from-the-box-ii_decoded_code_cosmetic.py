class Solution:
    def answerString(self, uniformEcho: str, criticCount: int) -> str:
        if criticCount == 1:
            return uniformEcho
        transitSecret = self._lastSubstring(uniformEcho)
        omegaByte = (len(uniformEcho) - criticCount) + 1
        # substring from index 1 (0-based 1 means second char) up to min length of transitSecret or omegaByte
        return transitSecret[1:1 + min(len(transitSecret), omegaByte)]

    def _lastSubstring(self, zag: str) -> str:
        alpha, beta, gamma = 0, 1, 0
        n = len(zag)
        while beta + gamma < n:
            if zag[alpha + gamma] == zag[beta + gamma]:
                gamma += 1
            else:
                if zag[alpha + gamma] > zag[beta + gamma]:
                    beta = beta + gamma + 1
                    gamma = 0
                else:
                    alpha = max(alpha + gamma + 1, beta)
                    beta = alpha + 1
                    gamma = 0
        return zag[alpha:]