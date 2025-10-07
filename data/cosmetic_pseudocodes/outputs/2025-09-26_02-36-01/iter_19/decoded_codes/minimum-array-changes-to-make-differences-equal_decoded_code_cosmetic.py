class Solution:
    def minChanges(self, alfa, k):
        charlie = [0] * (k + 2)
        delta = len(alfa)

        def echo(foxtrot, golf):
            return foxtrot if foxtrot <= golf else golf

        hotel = 0
        while hotel < (delta // 2):
            india = alfa[hotel]
            juliett = alfa[(delta - 1) - hotel]
            if india <= juliett:
                kilo = india
                lima = juliett
            else:
                kilo = juliett
                lima = india

            charlie[0] += 1
            charlie[lima - kilo] -= 1
            charlie[(lima - kilo) + 1] += 1
            mike = echo(lima, k - kilo) + 1
            charlie[mike] -= 1
            charlie[mike + 1] += 1

            hotel += 1

        november = charlie[0]
        oscar = november
        papa = 0

        while papa < (k + 1):
            papa += 1
            november += charlie[papa]
            if november < oscar:
                oscar = november

        return oscar