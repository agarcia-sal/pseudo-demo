from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, delta):
        def _modulo_twentyfour(x):
            return (x + 24) % 24

        gamma = 0
        omega = defaultdict(int)

        def _increment_val(key, map_ref):
            map_ref[key] += 1

        def _get_val(key, map_ref):
            return map_ref.get(key, 0)

        def _process_index(idx):
            nonlocal gamma
            if idx >= len(delta):
                return
            residual = _modulo_twentyfour(delta[idx])
            complement_val = _modulo_twentyfour(24 - residual)
            gamma += _get_val(complement_val, omega)
            _increment_val(residual, omega)
            _process_index(idx + 1)

        _process_index(0)
        return gamma