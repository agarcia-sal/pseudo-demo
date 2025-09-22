def doMain():
    # Step 2: Read input for the first sequence of values
    input1 = input()
    # Step 3: Read input for the second sequence of values
    input2 = input()
    
    # Step 4: Split input1 into a list of values
    values1 = input1.split()
    # Step 5: Split input2 into a list of values
    values2 = input2.split()
    
    # Step 6: Initialize a counter for differences
    differenceCount = 0
    
    # Step 7: Compare the first three elements of both lists
    for i in range(3):  # Looping from 0 to 2 inclusive
        # Convert values from both lists to integers
        value1 = int(values1[i])
        value2 = int(values2[i])
        
        # Step 7.4: Check if the values are different
        if value1 != value2:
            differenceCount += 1  # Increment the difference count if they are not equal
    
    # Step 8: Check the difference count
    if differenceCount < 3:
        print("YES")  # Print "YES" if fewer than 3 differences
    else:
        print("NO")   # Print "NO" if 3 or more differences

# Step 10: Call the doMain function if this script is executed directly
if __name__ == "__main__":
    doMain()
