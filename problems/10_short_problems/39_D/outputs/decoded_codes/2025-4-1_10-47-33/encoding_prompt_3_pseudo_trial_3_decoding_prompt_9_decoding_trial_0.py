def doMain():
    # Step 1: Read input values
    time1 = input()  # User input for first time
    time2 = input()  # User input for second time
    
    # Step 2: Split the input strings into components
    timeComponents1 = time1.split()  # Split the first time input based on whitespace
    timeComponents2 = time2.split()  # Split the second time input based on whitespace
    
    # Step 3: Initialize a counter for differences
    differenceCount = 0
    
    # Step 4: Compare each component of the two time inputs
    for index in range(3):  # Assuming there are exactly 3 components to compare
        component1 = int(timeComponents1[index])  # Convert the component to an integer
        component2 = int(timeComponents2[index])  # Convert the component to an integer
        
        # Step 5: Increment the counter if the components are different
        if component1 != component2:
            differenceCount += 1
    
    # Step 6: Output the result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    doMain()
