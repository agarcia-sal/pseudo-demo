def doMain():
    # Step 1: Read two lines of input and store them in variables
    t1 = input()  # First input string
    t2 = input()  # Second input string

    # Step 2: Split the input strings into lists of substrings
    tt1 = t1.split()  # Split the first input string into a list
    tt2 = t2.split()  # Split the second input string into a list

    # Step 3: Initialize a variable to count differences
    differenceCount = 0  # Count of differences between the two lists

    # Step 4: Compare elements of the two lists
    for index in range(3):  # Loop over the indices 0 to 2
        # Convert the substring to an integer for comparison
        a = int(tt1[index])  # Convert current element of tt1 to integer
        b = int(tt2[index])  # Convert current element of tt2 to integer

        # Step 5: Increment the count if the numbers are not equal
        if a != b:  # Check if the current elements are different
            differenceCount += 1  # Increment the difference count

    # Step 6: Determine output based on the number of differences
    if differenceCount < 3:  # If less than 3 differences
        print("YES")  # Output "YES"
    else:  # 3 or more differences
        print("NO")  # Output "NO"

# Step 7: Main execution block
if __name__ == "__main__":  # Check if the script is executed as the main program
    doMain()  # Call the main function
