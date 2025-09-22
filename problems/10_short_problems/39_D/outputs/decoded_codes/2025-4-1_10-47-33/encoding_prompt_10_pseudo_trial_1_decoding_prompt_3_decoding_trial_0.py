def do_main():
    # Step 1: Read input strings
    t1 = input()
    t2 = input()
    
    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 by whitespace
    tt2 = t2.split()  # Split t2 by whitespace
    
    # Step 3: Initialize a variable to count differences
    res = 0

    # Step 4: Loop through the first three elements of the lists
    for x in range(3):  # Steps through indices 0 to 2
        # Step 5: Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Step 6: Compare the values and increment difference count if not equal
        if a != b:
            res += 1
    
    # Step 7: Check the number of differences and print the result
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the main function when the script runs
do_main()


  1 2 3
  1 2 4
  

  YES
  

  5 6 7
  5 6 7
  

  YES
  

  8 9 10
  8 9 11
  

  NO
  