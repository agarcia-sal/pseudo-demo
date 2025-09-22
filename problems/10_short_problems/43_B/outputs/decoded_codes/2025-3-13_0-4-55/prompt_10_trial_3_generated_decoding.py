def main():
    # Step 2: Receive Input from User
    first_input = input()
    second_input = input()
    
    # Step 3: Initialize Lists
    s1 = [char for char in first_input if char != ' ']
    s2 = [char for char in second_input if char != ' ']
    
    # Step 4: Initialize Frequency Counter
    frequency_counter = [0] * 256  # ASCII range
    
    # Step 5: Calculate Character Frequencies
    for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
        char_in_s1_count = s1.count(chr(ascii_value))
        char_in_s2_count = s2.count(chr(ascii_value))
        frequency_counter[ascii_value] = char_in_s1_count - char_in_s2_count
    
    # Step 6: Determine if Frequencies are Non-Negative
    negative_count = sum(1 for count in frequency_counter if count < 0)
    
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to run the program
if __name__ == "__main__":
    main()
