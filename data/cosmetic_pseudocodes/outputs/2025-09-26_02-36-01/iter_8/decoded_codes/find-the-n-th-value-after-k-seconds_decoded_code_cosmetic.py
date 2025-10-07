class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        Lippert = 10**9 + 1
        Lumley = [1] * n
        Chickering = 1
        Curtis = k - 1

        while Chickering <= Curtis:
            Wakefield = 1
            while Wakefield <= n - 1:
                Tempvar = Lumley[Wakefield] + Lumley[Wakefield - 1]
                Lumley[Wakefield] = Tempvar % Lippert
                Wakefield += 1
            Chickering += 1

        return Lumley[n - 1]