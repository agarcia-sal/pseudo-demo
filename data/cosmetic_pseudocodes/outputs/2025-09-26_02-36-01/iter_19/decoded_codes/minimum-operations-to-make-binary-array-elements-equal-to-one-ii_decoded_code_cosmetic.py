class Solution:
    def minOperations(self, Sigma):
        Delta = 0
        Omega = 0

        def remainder_modulus(x, y):
            return x - y * (x // y)

        index = 0
        while index < len(Sigma):
            element = Sigma[index]
            temp_var = 0
            if remainder_modulus(Omega, 2) == 0:
                temp_var = element
            else:
                temp_var = 1 - element
            if temp_var == 0:
                Delta += 1
                Omega += 1
            index += 1

        return Delta