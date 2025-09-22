def main():
    # Step 1: Read input
    firstString = input()
    secondString = input()

    # Step 2: Remove spaces from both strings
    filteredFirstString = [char for char in firstString if char != ' ']
    filteredSecondString = [char for char in secondString if char != ' ']

    # Step 3: Count character frequency differences
    frequencyDifferences = []

    for characterCode in range(ord('A'), ord('z') + 1):
        character = chr(characterCode)
        countInFirstString = filteredFirstString.count(character)
        countInSecondString = filteredSecondString.count(character)
        difference = countInFirstString - countInSecondString
        frequencyDifferences.append(difference)

    # Step 4: Check if any frequency difference is negative
    hasNegativeDifference = any(difference < 0 for difference in frequencyDifferences)

    # Step 5: Output the result
    if not hasNegativeDifference:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
