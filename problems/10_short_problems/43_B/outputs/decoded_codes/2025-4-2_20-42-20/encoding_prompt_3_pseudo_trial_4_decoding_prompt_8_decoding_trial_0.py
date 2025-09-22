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
        firstStringCount = cleanedFirstString.count(chr(characterCode))
        secondStringCount = cleanedSecondString.count(chr(characterCode))
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

# Example of testing the function
if __name__ == "__main__":
    check_strings_difference()


from collections import Counter

def check_strings_difference():
    firstString = input()
    secondString = input()

    cleanedFirstString = ''.join(firstString.split())
    cleanedSecondString = ''.join(secondString.split())

    firstCounter = Counter(cleanedFirstString)
    secondCounter = Counter(cleanedSecondString)

    # Calculate frequency difference
    frequencyDifference = [firstCounter[chr(code)] - secondCounter[chr(code)] for code in range(ord('A'), ord('z') + 1)]

    # No need for a separate count, just check conditions
    if all(diff >= 0 for diff in frequencyDifference):
        print("YES")
    else:
        print("NO")
