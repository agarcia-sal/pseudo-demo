class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        omega = {}
        alpha = {}
        i = 0
        while i < len(word):
            ch = word[i]
            if ch not in omega:
                omega[ch] = i
            alpha[ch] = i
            i += 1

        kappa = 0
        gamma = 0
        delta = "abcdefghijklmnopqrstuvwxyz"
        eta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        while True:
            if gamma >= len(delta):
                break
            a_char = delta[gamma]
            b_char = eta[gamma]
            if a_char in alpha and b_char in omega:
                if omega[b_char] < alpha[a_char]:
                    kappa += 1
            gamma += 1

        return kappa