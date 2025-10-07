def common(listOne, listTwo):
    commonElements = set()
    for elementOne in listOne:
        for elementTwo in listTwo:
            if elementOne == elementTwo:
                commonElements.add(elementOne)
    return sorted(commonElements)