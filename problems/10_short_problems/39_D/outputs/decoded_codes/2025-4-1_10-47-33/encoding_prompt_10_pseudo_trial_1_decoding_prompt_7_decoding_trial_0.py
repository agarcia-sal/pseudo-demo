def doMain():
    # Step 1: Read input strings
    t1 = input()  # User input for the first string
    t2 = input()  # User input for the second string

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split the first input by whitespace
    tt2 = t2.split()  # Split the second input by whitespace

    # Step 3: Initialize a variable to count differences
    res = 0  # Counter for the differences

    # Step 4: Loop through the first three elements of the lists
    for x in range(3):  # Loop over indices 0 to 2
        # Step 5: Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of the first list to an integer
        b = int(tt2[x])  # Convert the x-th element of the second list to an integer
        
        # Step 6: Compare the values and increment difference count if not equal
        if a != b:  # Check if the integers are not equal
            res += 1  # Increment the difference counter

    # Step 7: Check the number of differences and print the result
    if res < 3:  # If there are fewer than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")   # Output "NO"

# Step 8: Execute the main function when the script runs
doMain()


  1 2 3
  1 2 3
  

  1 2 3
  1 2 4
  

  1 2 3
  0 2 4
  

  1 2 3
  4 5 6
  