def doMain():
    # Step 2: Read input for the first sequence of values
    input1 = input()
    
    # Step 3: Read input for the second sequence of values
    input2 = input()
    
    # Step 4: Split input1 into a list of values
    values1 = input1.split()
    
    # Step 5: Split input2 into a list of values
    values2 = input2.split()
    
    # Step 6: Initialize a counter variable
    differenceCount = 0
    
    # Step 7: For each index i from 0 to 2 (inclusive)
    for i in range(3):
        value1 = int(values1[i])  # Convert values1[i] to integer
        value2 = int(values2[i])  # Convert values2[i] to integer
        
        # If value1 is not equal to value2
        if value1 != value2:
            differenceCount += 1  # Increment differenceCount by 1
    
    # Step 8: If differenceCount is less than 3
    if differenceCount < 3:
        print("YES")  # Print "YES"
    else:
        print("NO")   # Step 9: Else, print "NO"

# Step 10: If the script is executed directly
if __name__ == "__main__":
    doMain()  # Call the doMain function
