# This code finds the length of the longest prefix of a given string
# that appears again as a substring later in the string.

def main():
    # Read a line of input (string)
    inputString = input()

    # Get the length of the input string
    stringLength = len(inputString)

    # Initialize a variable to store the longest prefix length found
    longestPrefixLength = 0

    # Loop through potential prefix lengths from 0 up to stringLength
    for currentLength in range(stringLength):
        # Check every starting position in the string
        for startPosition in range(stringLength):
            # Ensure we only check for prefixes that can exist
            if startPosition + currentLength <= stringLength:
                # Extract the current prefix substring
                currentPrefix = inputString[startPosition:startPosition + currentLength]

                # Check if the substring exists again elsewhere in the string
                foundIndex = inputString.find(currentPrefix, startPosition + 1)
                
                # If found, update the longest prefix length
                if foundIndex != -1:
                    longestPrefixLength = currentLength
                    break  # Found a match, no need to check further in this iteration
        
        # If a match was found, break out of the currentLength loop
        if longestPrefixLength == currentLength:
            continue  # No need to check longer prefixes, exit early

    # Output the length of the longest prefix found
    print(longestPrefixLength)

# Call the main function to execute the code
main()
