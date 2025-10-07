class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        def duplicate(x: int) -> int:
            return x + x

        def halve(x: int) -> int:
            return x // 2  # integer division

        def nextLetter(c: str) -> str:
            startChar = 'a'
            endChar = 'z'
            code = ord(c)
            nextCode = code + 1
            if nextCode > ord(endChar):
                nextCode = ord(startChar)
            return chr(nextCode)

        omega = 1
        sigma = []

        def populateSigma(lst: list[int]):
            def iterate(index: int):
                if index >= len(lst):
                    return
                sigma.append(lst[index])
                # The pseudocode increases omega by doubling at each append regardless of value (0 or not 0)
                # Because condition is "if lst[index] = 0 or lst[index] <> 0" - always true
                nonlocal omega
                omega = duplicate(omega)
                iterate(index + 1)
            iterate(0)
        populateSigma(param_operations)

        phi = 'a'

        def descend(i: int, k_ref: list[int], omega_ref: list[int]):
            if i < 0:
                return
            if k_ref[0] <= halve(omega_ref[0]):
                omega_ref[0] = halve(omega_ref[0])
                descend(i - 1, k_ref, omega_ref)
            else:
                k_ref[0] -= halve(omega_ref[0])
                omega_ref[0] = halve(omega_ref[0])
                if sigma[i] == 1:
                    nonlocal phi
                    phi = nextLetter(phi)
                descend(i - 1, k_ref, omega_ref)

        refK = [param_k]
        refOmega = [omega]
        descend(len(sigma) - 1, refK, refOmega)

        return phi