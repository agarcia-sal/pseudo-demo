class Solution:
    def minValidStrings(self, tangoFoxtrot, whiskeyZulu):
        def collectPrefixes(alphaBravo):
            kiloLima = set()

            def accumulate(charlie):
                def innerAccumulate(deltaEcho):
                    if deltaEcho > len(charlie):
                        return
                    kiloLima.add(charlie[:deltaEcho])
                    innerAccumulate(deltaEcho + 1)
                innerAccumulate(1)

            while alphaBravo:
                hotelIndia = alphaBravo.pop(0)
                accumulate(hotelIndia)
            return kiloLima

        def getMin(a, b):
            return a if a < b else b

        kiloLima = collectPrefixes(tangoFoxtrot)
        uniformVictor = len(whiskeyZulu)
        yankeeXray = [10**9] * (uniformVictor + 1)
        yankeeXray[0] = 0

        def substringExists(bravoChar, charStart, charEnd):
            return bravoChar[charStart:charEnd] in kiloLima

        def fillDP(index):
            if index > uniformVictor:
                return
            juliettTango = 1
            while juliettTango <= index:
                subStr = whiskeyZulu[juliettTango - 1:index]
                if subStr in kiloLima:
                    yankeeXray[index] = getMin(yankeeXray[index], yankeeXray[juliettTango - 1] + 1)
                juliettTango += 1
            fillDP(index + 1)

        fillDP(1)

        return yankeeXray[uniformVictor] if yankeeXray[uniformVictor] != 10**9 else -1