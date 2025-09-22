# BEGIN

# Step 1: Read input
# Get user input for the first string and second string
firstString = input()
secondString = input()

# Step 2: Remove spaces from both strings
# Initialize lists to hold characters without spaces
filteredFirstString = []
filteredSecondString = []

# Filter out spaces from the first string
for character in firstString:
    if character != ' ':
        filteredFirstString.append(character)

# Filter out spaces from the second string
for character in secondString:
    if character != ' ':
        filteredSecondString.append(character)

# Step 3: Count character frequency differences
# List to hold the frequency differences of characters
frequencyDifferences = []

# Iterate over all ASCII characters from 'A' to 'z'
for characterCode in range(ord('A'), ord('z') + 1):
    character = chr(characterCode)
    countInFirstString = filteredFirstString.count(character)  # count occurrences in the first filtered string
    countInSecondString = filteredSecondString.count(character)  # count occurrences in the second filtered string
    difference = countInFirstString - countInSecondString  # calculate the difference
    frequencyDifferences.append(difference)  # store the difference

# Step 4: Check if any frequency difference is negative
hasNegativeDifference = False

# Iterate through frequency differences to check for negativity
for difference in frequencyDifferences:
    if difference < 0:
        hasNegativeDifference = True
        break  # Exit the loop if a negative difference is found

# Step 5: Output the result
if hasNegativeDifference == False:
    print("YES")  # Print YES if no negative differences are found
else:
    print("NO")   # Print NO if any negative differences are found

# END
