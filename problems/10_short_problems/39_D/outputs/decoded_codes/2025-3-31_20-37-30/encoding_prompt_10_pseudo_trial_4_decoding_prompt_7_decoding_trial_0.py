def doMain():
    # Step 1: Take two inputs
    t1 = input()  # User input for first list
    t2 = input()  # User input for second list

    # Step 2: Split inputs into lists of strings
    tt1 = t1.split()  # Convert the first input into a list of strings
    tt2 = t2.split()  # Convert the second input into a list of strings

    # Step 3: Initialize a result counter
    res = 0 

    # Step 4: Loop through the first three elements of the lists
    for index in range(3):
        # Convert string elements to integers
        a = int(tt1[index])  # Convert the element from the first list to integer
        b = int(tt2[index])  # Convert the element from the second list to integer
        
        # Step 5: Compare the numbers and update the counter
        if a != b:  # Check if the numbers are not equal
            res += 1  # Increment the result counter

    # Step 6: Check the result counter
    if res < 3:  # If the difference is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 7: Execute the doMain function if this script is run as the main program
if __name__ == "__main__":
    doMain()  # Call the main function
