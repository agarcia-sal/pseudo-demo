# BEGIN

# Read two input strings
firstString = input()
secondString = input()

# Function to remove spaces from a string
def REMOVE_SPACES(inputString):
    return ''.join([char for char in inputString if char != ' '])

# Remove spaces from each string and store the results in s1 and s2
s1 = REMOVE_SPACES(firstString)
s2 = REMOVE_SPACES(secondString)

# Initialize a list to hold the frequency differences between the two strings
frequencyDifferences = []

# For each character in the ASCII range from 'A' to 'z'
for characterCode in range(ord('A'), ord('z') + 1):  # +1 because range is exclusive
    # Function to count occurrences of a character in a string
    def COUNT_CHARACTER(string, characterCode):
        return string.count(chr(characterCode))

    # Calculate the frequency of the character in s1 and s2
    frequencyInS1 = COUNT_CHARACTER(s1, characterCode)
    frequencyInS2 = COUNT_CHARACTER(s2, characterCode)

    # Calculate the difference in frequencies and add to the list
    frequencyDifference = frequencyInS1 - frequencyInS2
    frequencyDifferences.append(frequencyDifference)

# Function to count negative differences
def COUNT_NEGATIVE(list):
    return sum(1 for x in list if x < 0)

# Check if there are any negative differences in the frequency list
if COUNT_NEGATIVE(frequencyDifferences) == 0:
    print("YES")
else:
    print("NO")

# END
