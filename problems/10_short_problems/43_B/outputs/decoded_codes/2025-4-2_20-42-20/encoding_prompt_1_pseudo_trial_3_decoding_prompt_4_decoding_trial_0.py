def main():
    # Step 1: Input two strings
    first_string = input()
    second_string = input()
    
    # Step 2: Process the strings to remove spaces
    first_string_processed = ''.join(char for char in first_string if char != ' ')
    second_string_processed = ''.join(char for char in second_string if char != ' ')
    
    # Step 3: Initialize a frequency list
    frequency_difference = []

    # Step 4: Calculate the frequency difference
    for char in range(ord('A'), ord('z') + 1):
        char_count_first = first_string_processed.count(chr(char))
        char_count_second = second_string_processed.count(chr(char))
        frequency_difference.append(char_count_first - char_count_second)
    
    # Step 5: Check the frequency list for negative values
    negative_count = sum(1 for count in frequency_difference if count < 0)

    # Step 6: Output the result
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
