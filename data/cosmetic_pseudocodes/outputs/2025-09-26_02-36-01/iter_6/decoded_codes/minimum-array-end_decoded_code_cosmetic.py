class Solution:
    def minEnd(self, var_a: int) -> int:
        def canConstruct(var_b: int) -> bool:
            def bitwiseAnd(val1: int, val2: int) -> int:
                return val1 & val2

            var_c = var_a
            var_d = 1
            conditionMet = False

            while not conditionMet:
                if var_c < var_b:
                    var_c += 1
                    if bitwiseAnd(var_c, var_a) == var_a:
                        var_d += 1
                        if var_d == n:
                            conditionMet = True
                else:
                    conditionMet = True
            return var_d == n

        var_e = var_a
        helperMul = 2 * 10
        var_f = helperMul * 10 ** 7
        var_g = False

        n = self.n  # Note: n must be set before calling minEnd, since pseudocode uses it in canConstruct

        while not var_g:
            if var_e < var_f:
                var_h = (var_e + var_f) // 2
                if canConstruct(var_h):
                    var_f = var_h
                else:
                    var_e += 1
            else:
                var_g = True
        return var_e