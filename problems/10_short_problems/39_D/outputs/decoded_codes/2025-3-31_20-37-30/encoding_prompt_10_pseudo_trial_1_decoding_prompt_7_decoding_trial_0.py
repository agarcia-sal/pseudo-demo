def main():
    # Step 1: Receive user input for two strings
    t1 = input()
    t2 = input()
    
    # Step 2: Split input strings into lists of strings
    tt1 = t1.split()  # Split the first input string into words
    tt2 = t2.split()  # Split the second input string into words
    
    # Step 3: Initialize the result counter
    res = 0
    
    # Step 4: Loop through the first three elements of both lists
    for index in range(3):  # Loop from index 0 to 2
        # Step 5: Convert string elements to integers
        a = int(tt1[index])  # Convert the element from the first list
        b = int(tt2[index])  # Convert the element from the second list
        
        # Step 6: Check for inequality
        if a != b:  # If the values are not equal
            res += 1  # Increment the result counter
    
    # Step 7: Determine output based on the result counter
    if res < 3:  # If less than 3 mismatches
        print("YES")  # Print "YES"
    else:
        print("NO")  # Print "NO" if there are 3 or more mismatches

# Step 8: Run Main function when the program starts
if __name__ == "__main__":  # Check if this script is executed directly
    main()  # Call the main function
