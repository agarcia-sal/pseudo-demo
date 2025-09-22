def main():
    # Step 1: Receive Input
    first_string = input()
    second_string = input()

    # Step 2: Process Input Strings
    first_processed = first_string.replace(" ", "")
    second_processed = second_string.replace(" ", "")

    # Step 3: Initialize Frequency List
    frequency_difference = [0] * (ord('z') - ord('A') + 1)

    # Step 4: Calculate Character Frequencies
    for char_code in range(ord('A'), ord('z') + 1):
        count_first = first_processed.count(chr(char_code))
        count_second = second_processed.count(chr(char_code))
        
        # Calculate the difference and store it in the frequency_difference list
        frequency_difference[char_code - ord('A')] = count_first - count_second

    # Step 5: Check Conditions
    negative_count = sum(1 for diff in frequency_difference if diff < 0)

    if negative_count == 0:
        print("YES")  # All characters in firstProcessed meet/exceed counts in secondProcessed
    else:
        print("NO")   # Some characters in secondProcessed exceed those in firstProcessed

# Call the main function
main()
