def compareStringFrequencies():
    # Prompt user for input strings
    firstInputString = input()
    secondInputString = input()
    
    # Remove spaces from both input strings
    firstProcessedString = [char for char in firstInputString if char != ' ']
    secondProcessedString = [char for char in secondInputString if char != ' ']
    
    # Initialize a list to hold frequency differences
    frequencyDifferences = []
    
    # Calculate the frequency difference for each character in the range of 'A' to 'z'
    for characterCode in range(ord('A'), ord('z') + 1):
        firstStringCount = firstProcessedString.count(chr(characterCode))
        secondStringCount = secondProcessedString.count(chr(characterCode))
        # Calculate the difference in frequency between both strings
        frequencyDifferences.append(firstStringCount - secondStringCount)
    
    # Check if there are any negative frequency differences
    negativeCounts = [count for count in frequencyDifferences if count < 0]
    
    # Print "YES" if no negative frequencies are found, otherwise print "NO"
    if len(negativeCounts) == 0:
        print("YES")
    else:
        print("NO")

# Note: The function can be called, and it will wait for user input
