def compareStringsForCharacterBalance():
    # INPUT: Read two strings from user
    firstString = input()
    secondString = input()
    
    # INITIALIZE: Create character lists without spaces
    firstCharacterList = [char for char in firstString if char != ' ']
    secondCharacterList = [char for char in secondString if char != ' ']

    # INITIALIZE: Create a list to store frequency differences
    frequencyDifferences = []

    # CALCULATE frequency differences for each character in the range A to z
    for characterCode in range(ord('A'), ord('z') + 1):
        # Count occurrences of character in both lists
        countInFirst = firstCharacterList.count(chr(characterCode))
        countInSecond = secondCharacterList.count(chr(characterCode))
        
        # Calculate frequency difference
        frequencyDifference = countInFirst - countInSecond
        # Add frequency difference to the list
        frequencyDifferences.append(frequencyDifference)

    # CHECK: Determine if all frequency differences are non-negative
    if all(difference >= 0 for difference in frequencyDifferences):
        print("YES")
    else:
        print("NO")

# Example test cases for verification
if __name__ == "__main__":
    # Uncomment to test
    # Test case 1
    # Input: "abc", "a"
    # Output: "YES"
    
    # Test case 2
    # Input: "aabbcc", "abc"
    # Output: "YES"
    
    # Test case 3
    # Input: "abc", "abcc"
    # Output: "NO"

    # Call the function to execute
    compareStringsForCharacterBalance()
