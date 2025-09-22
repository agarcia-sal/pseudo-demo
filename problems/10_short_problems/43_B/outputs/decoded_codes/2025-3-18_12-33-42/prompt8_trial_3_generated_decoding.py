def CompareStringFrequencies():
    # Step 1: Read Input
    firstString = input()
    secondString = input()
    
    # Step 2: Clean Input
    cleanedFirstString = firstString.replace(" ", "")
    cleanedSecondString = secondString.replace(" ", "")
    
    # Step 3: Create Frequency Difference List
    frequencyDifferences = []
    for asciiValue in range(65, 123):  # A-Z and a-z
        firstCount = cleanedFirstString.count(chr(asciiValue))
        secondCount = cleanedSecondString.count(chr(asciiValue))
        frequencyDifferences.append(firstCount - secondCount)

    # Step 4: Check for Negative Frequencies
    negativeCount = 0
    for value in frequencyDifferences:
        if value < 0:
            negativeCount += 1
    
    # Step 5: Determine Result
    if negativeCount == 0:
        print("YES")
    else:
        print("NO")

# Example usage
CompareStringFrequencies()
