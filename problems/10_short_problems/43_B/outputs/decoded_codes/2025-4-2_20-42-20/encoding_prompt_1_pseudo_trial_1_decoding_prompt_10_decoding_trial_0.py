def main():
    # Step 1: Input two strings from the user
    first_string = input()
    second_string = input()
    
    # Step 2: Process Input - Removing all spaces
    cleaned_first = first_string.replace(" ", "")
    cleaned_second = second_string.replace(" ", "")
    
    # Step 3: Initialize Frequency Difference List
    frequency_differences = []
    
    # Step 4: Count Character Frequencies
    for char in range(ord('A'), ord('z') + 1):
        count_in_first = cleaned_first.count(chr(char))
        count_in_second = cleaned_second.count(chr(char))
        frequency_difference = count_in_first - count_in_second
        frequency_differences.append(frequency_difference)
    
    # Step 5: Check Frequency Differences
    negative_count = sum(1 for difference in frequency_differences if difference < 0)
    
    # Step 6: Output Result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
