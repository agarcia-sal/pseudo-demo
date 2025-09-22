def CompareStrings():
    # Read User Input
    firstString = input()
    secondString = input()
    
    # Remove Spaces
    firstString = firstString.replace(" ", "")
    secondString = secondString.replace(" ", "")
    
    # Initialize Frequency List
    frequencyDifferences = []
    
    # For Each Character in the Range from ASCII of 'A' to ASCII of 'z'
    for char in range(ord('A'), ord('z') + 1):
        charInFirst = firstString.count(chr(char))
        charInSecond = secondString.count(chr(char))
        
        # Calculate Difference
        Difference = charInFirst - charInSecond
        frequencyDifferences.append(Difference)
    
    # Check for Non-Negative Counts
    negativeCount = sum(1 for count in frequencyDifferences if count < 0)
    
    # Output Result
    if negativeCount == 0:
        print("YES")
    else:
        print("NO")

# Example of how to call the function
CompareStrings()
