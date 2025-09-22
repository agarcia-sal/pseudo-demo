def main():
    # Step 1: Get Input
    firstString = input()
    secondString = input()

    # Step 2: Process Input
    processedFirstString = []
    processedSecondString = []
    for char in firstString:
        if char != ' ':
            processedFirstString.append(char)
    for char in secondString:
        if char != ' ':
            processedSecondString.append(char)

    # Step 3: Frequency Calculation
    frequencyDifferences = []
    for char_code in range(ord('A'), ord('z') + 1):
        count_first = processedFirstString.count(chr(char_code))
        count_second = processedSecondString.count(chr(char_code))
        frequencyDifferences.append(count_first - count_second)

    # Step 4: Condition Check and Output
    # Check if there's any negative value in frequencyDifferences
    if any(diff < 0 for diff in frequencyDifferences):
        print("NO")
    else:
        print("YES")

# Execute the main function
if __name__ == "__main__":
    main()
