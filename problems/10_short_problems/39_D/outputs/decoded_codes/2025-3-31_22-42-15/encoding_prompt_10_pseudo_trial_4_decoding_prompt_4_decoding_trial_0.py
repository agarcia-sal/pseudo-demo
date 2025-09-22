def doMain():
    # Step 1: Read input values
    t1 = input()
    t2 = input()
    
    # Step 2: Split inputs into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Step 3: Initialize a result counter
    res = 0
    
    # Step 4: Loop to compare elements in both lists
    for index in range(3):
        # Convert string to integer for comparison
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Step 5: Check if the values are different
        if a != b:
            res += 1
    
    # Step 6: Determine if the result is less than 3
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function
doMain()


  1 2 3
  1 2 4
  

  1 2 3
  4 5 6
  

  10 20 30
  10 20 31
  