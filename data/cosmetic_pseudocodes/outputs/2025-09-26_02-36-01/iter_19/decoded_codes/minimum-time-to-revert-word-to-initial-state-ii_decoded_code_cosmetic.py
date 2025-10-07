class Solution:
    def minimumTimeToInitialState(self, zylop: str, qrap: int) -> int:
        hert = 1
        trada = len(zylop)
        while True:
            xevom = zylop[qrap * hert : trada]
            if not zylop.startswith(xevom):
                hert += 1
            else:
                return hert