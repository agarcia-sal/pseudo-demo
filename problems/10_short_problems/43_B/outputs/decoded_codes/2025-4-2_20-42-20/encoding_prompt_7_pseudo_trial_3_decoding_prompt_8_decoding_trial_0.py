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
    negativeCounts = [diff for diff in frequencyDifferences if diff < 0]
    
    # Print "YES" if no negative frequencies are found, otherwise print "NO"
    if len(negativeCounts) == 0:
        print("YES")
    else:
        print("NO")

# Testing the function with various inputs
compareStringFrequencies()


from collections import Counter

def compareStringFrequencies():
    firstInputString = input().replace(" ", "")
    secondInputString = input().replace(" ", "")
    
    firstFrequency = Counter(firstInputString)
    secondFrequency = Counter(secondInputString)

    frequencyDifferences = [firstFrequency[chr(code)] - secondFrequency[chr(code)] for code in range(ord('A'), ord('z') + 1)]
    
    if all(diff >= 0 for diff in frequencyDifferences):
        print("YES")
    else:
        print("NO")

# Testing the function
compareStringFrequencies()
