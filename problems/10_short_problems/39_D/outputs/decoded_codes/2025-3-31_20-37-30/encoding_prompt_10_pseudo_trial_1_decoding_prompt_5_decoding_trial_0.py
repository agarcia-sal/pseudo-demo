def main():
    # Step 1: Receive user input
    input1 = input()  # First user input
    input2 = input()  # Second user input
    
    # Step 2: Split input strings into lists of words
    words_list1 = input1.split()  # List from first input
    words_list2 = input2.split()  # List from second input
    
    # Step 3: Initialize the result counter
    result_counter = 0
    
    # Step 4: Loop through the first three elements of both lists
    for index in range(3):  # From 0 to 2 (inclusive)
        # Step 5: Convert string elements to integers
        num1 = int(words_list1[index])  # Convert first list element to integer
        num2 = int(words_list2[index])  # Convert second list element to integer
        
        # Step 6: Check for inequality
        if num1 != num2:  # If elements are not equal
            result_counter += 1  # Increment result counter
    
    # Step 7: Determine output based on the result counter
    if result_counter < 3:  # If less than 3 elements differ
        print("YES")  # Print YES
    else:
        print("NO")  # Print NO

# Step 8: Run Main function when the program starts
if __name__ == "__main__":
    main()  # Call the main function
