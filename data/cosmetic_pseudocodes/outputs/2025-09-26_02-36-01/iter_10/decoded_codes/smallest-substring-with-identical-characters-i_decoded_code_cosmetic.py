class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(s):
            def internal_max(a, b):
                return a if a >= b else b

            alpha = 0
            beta = 1
            gamma = 1
            delta = len(s) - 1

            while beta <= delta:
                if s[beta] == s[beta - 1]:
                    gamma += 1
                else:
                    alpha = internal_max(alpha, gamma)
                    gamma = 1
                beta += 1

            return internal_max(alpha, gamma)

        def bit_count(x):
            c = 0
            z = x
            while z != 0:
                c += z & 1
                z >>= 1
            return c

        def apply_flips(original_list, mask):
            flipped_list = []
            idx = 0
            length = len(original_list)
            while idx < length:
                if (mask & (1 << idx)) != 0:
                    flipped_list.append('1' if original_list[idx] == '0' else '0')
                else:
                    flipped_list.append(original_list[idx])
                idx += 1
            return flipped_list

        epsilon = len(s)
        zeta = (1 << len(s)) - 1
        eta = 0

        while eta <= zeta:
            if bit_count(eta) > numOps:
                eta += 1
                continue

            omega = apply_flips(list(s), eta)
            psi = longest_uniform_substring(omega)

            if epsilon > psi:
                epsilon = psi

            eta += 1

        return epsilon