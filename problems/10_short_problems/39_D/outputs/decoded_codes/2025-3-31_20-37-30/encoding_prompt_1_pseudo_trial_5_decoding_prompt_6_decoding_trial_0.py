def doMain():
    # Step 2: Read input for the first sequence of values
    input1 = input()
    
    # Step 3: Read input for the second sequence of values
    input2 = input()
    
    # Step 4: Split input1 into a list of values
    values1 = input1.split()
    
    # Step 5: Split input2 into a list of values
    values2 = input2.split()
    
    # Step 6: Initialize a counter variable for differences
    difference_count = 0
    
    # Step 7: Compare elements from both value lists
    for i in range(3):  # Looping through indices 0 to 2 (inclusive)
        # Convert and store the values from both lists
        value1 = int(values1[i])
        value2 = int(values2[i])
        
        # Check if the values are not equal and increment the counter if so
        if value1 != value2:
            difference_count += 1

    # Step 8: Print result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 10: Call the function if this script is executed directly
if __name__ == "__main__":
    doMain()
