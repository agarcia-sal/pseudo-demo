def main():
    # Step 2: Receive Input from User
    first_input = input()
    second_input = input()

    # Step 3: Initialize Lists by Removing Spaces
    s1 = [char for char in first_input if char != ' ']
    s2 = [char for char in second_input if char != ' ']

    # Step 4: Initialize Frequency Counter
    frequency_count = [0] * 256  # Array to store counts for ASCII characters

    # Step 5: Calculate Character Frequencies
    for ascii_value in range(65, 123):  # Iterate over A to z
        count_in_s1 = s1.count(chr(ascii_value))
        count_in_s2 = s2.count(chr(ascii_value))

        # Calculate the difference and store in frequency_count
        frequency_count[ascii_value] = count_in_s1 - count_in_s2

    # Step 6: Determine if Frequencies are Non-Negative
    negative_count = sum(1 for count in frequency_count if count < 0)

    # Step 6 continued: Print Results
    if negative_count == 0:
        print("YES")  # If no negative frequencies
    else:
        print("NO")  # If any negative frequencies

# Step 1: Start Program
if __name__ == "__main__":
    main()


   hello
   hello
   

   YES
   

   a
   A
   

   NO
   

   A B C
   A B D
   

   NO
   

   abcde
   edcba
   

   YES
   