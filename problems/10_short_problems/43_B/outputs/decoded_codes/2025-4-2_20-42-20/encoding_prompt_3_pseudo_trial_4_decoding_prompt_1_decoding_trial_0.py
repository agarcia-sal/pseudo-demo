def check_strings_difference():
    
    # Input: Two strings from the user
    firstString = input()
    secondString = input()
    
    # Process: Remove spaces from both strings
    cleanedFirstString = [char for char in firstString if char != ' ']
    cleanedSecondString = [char for char in secondString if char != ' ']

    # Initialize frequency difference list
    frequencyDifference = []

    # Calculate frequency difference for each character in the ASCII range from 'A' to 'z'
    for characterCode in range(ord('A'), ord('z') + 1):
        char = chr(characterCode)
        firstStringCount = cleanedFirstString.count(char)
        secondStringCount = cleanedSecondString.count(char)
        difference = firstStringCount - secondStringCount

        # Append the difference to the frequency difference list
        frequencyDifference.append(difference)

    # Determine if any frequency difference is negative
    negativeCount = sum(1 for diff in frequencyDifference if diff < 0)

    # Output: Print "YES" if all frequency differences are non-negative, otherwise print "NO"
    if negativeCount == 0:
        print("YES")
    else:
        print("NO")
