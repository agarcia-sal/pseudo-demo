def main():
    # Initialize first string
    firstString = input()
    firstString = firstString.replace(" ", "")
    
    # Initialize second string
    secondString = input()
    secondString = secondString.replace(" ", "")
    
    # Create empty list for characterFrequencyDifference
    characterFrequencyDifference = []
    
    # Store character frequencies
    for characterCode in range(ord('A'), ord('z') + 1):
        countInFirst = firstString.count(chr(characterCode))
        countInSecond = secondString.count(chr(characterCode))
        difference = countInFirst - countInSecond
        characterFrequencyDifference.append(difference)
    
    # Count negative frequencies
    negativeFrequencyCount = 0
    for frequency in characterFrequencyDifference:
        if frequency < 0:
            negativeFrequencyCount += 1
    
    # Provide output
    if negativeFrequencyCount == 0:
        print("YES")
    else:
        print("NO")

# This calls the main function to execute the program
main()
