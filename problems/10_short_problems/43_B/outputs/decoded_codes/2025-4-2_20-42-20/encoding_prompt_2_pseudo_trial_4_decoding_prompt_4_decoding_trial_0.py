def main():
    # Step 1: Receive Input
    cleanedString1 = input().replace(" ", "")
    cleanedString2 = input().replace(" ", "")
    
    # Step 2: Initialize Frequency List
    frequencyDifferences = []
    
    # Step 3: Calculate Frequency Differences
    for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
        char = chr(ascii_value)
        count_in_string1 = cleanedString1.count(char)
        count_in_string2 = cleanedString2.count(char)
        difference = count_in_string1 - count_in_string2
        frequencyDifferences.append(difference)
    
    # Step 4: Check for Negative Differences
    negative_differences = [diff for diff in frequencyDifferences if diff < 0]
    
    if not negative_differences:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
