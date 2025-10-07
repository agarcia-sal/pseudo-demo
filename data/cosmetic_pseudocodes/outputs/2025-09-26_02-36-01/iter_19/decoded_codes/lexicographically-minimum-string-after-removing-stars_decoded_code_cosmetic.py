class Solution:
    def clearStars(self, s: str) -> str:
        beta = []
        gamma = 0
        while gamma < len(s):
            omega = s[gamma]
            if omega != "*":
                beta.append(omega)
            else:
                if beta:
                    beta.pop()
            gamma += 1
        delta = ""
        epsilon = 0
        while True:
            if epsilon == len(beta):
                break
            delta += beta[epsilon]
            epsilon += 1
        final_output = delta
        return final_output