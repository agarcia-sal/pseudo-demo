class Solution:
    def findWinningPlayer(self, totals, threshold):
        limit = len(totals)
        collection = []

        def fillCollection():
            index = 0
            while index != limit:
                collection.append(index)
                index += 1

        fillCollection()

        successCount = 0
        champion = collection.pop(0)
        while successCount < threshold and len(collection) > 0:
            challenger = collection.pop(0)
            if totals[champion] > totals[challenger]:
                successCount += 1
                collection.append(challenger)
            else:
                successCount = 1
                collection.append(champion)
                champion = challenger

        return champion