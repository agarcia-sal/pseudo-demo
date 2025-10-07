class Solution:
    def kthCharacter(self, param_y: int, param_z: list[int]) -> str:
        var_f = 1
        var_m = []

        var_n = 0
        while var_n < len(param_z):
            var_m.append(param_z[var_n])
            var_f *= 2
            var_n += 1

        var_w = 'a'
        var_r = len(var_m) - 1

        while var_r >= 0:
            half = var_f // 2
            if param_y <= half:
                var_f = half
            else:
                param_y -= half
                var_f = half
                if var_m[var_r] == 1:
                    var_w = chr(((ord(var_w) - ord('a') + 1) % 26) + ord('a'))
            var_r -= 1

        return var_w