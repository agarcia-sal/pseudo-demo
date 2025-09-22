def check_strings_difference():
    # Input: Two strings from the user
    firstString = input()  # Prompt for first string
    secondString = input()  # Prompt for second string

    # Process: Remove spaces from both strings
    cleanedFirstString = [char for char in firstString if char != ' ']  # List of characters excluding spaces
    cleanedSecondString = [char for char in secondString if char != ' ']  # List of characters excluding spaces

    # Initialize frequency difference list
    frequencyDifference = []  # Will hold the frequency difference for each character

    # Calculate frequency difference for each character in the ASCII range from 'A' to 'z'
    for characterCode in range(ord('A'), ord('z') + 1):  # Covering ASCII from 'A' to 'z'
        char = chr(characterCode)
        firstStringCount = cleanedFirstString.count(char)  # Count occurrences in firstString
        secondStringCount = cleanedSecondString.count(char)  # Count occurrences in secondString
        difference = firstStringCount - secondStringCount  # Calculate difference
        
        # Append the difference to the frequency difference list
        frequencyDifference.append(difference)

    # Determine if any frequency difference is negative
    # If no character has more occurrences in the second string than the first
    negativeCount = sum(1 for diff in frequencyDifference if diff < 0)  # Count negative differences

    # Output: Print "YES" if all frequency differences are non-negative, otherwise print "NO"
    if negativeCount == 0:
        print("YES")
    else:
        print("NO")

# Example of calling the function (uncomment the below line to run)
# check_strings_difference()
