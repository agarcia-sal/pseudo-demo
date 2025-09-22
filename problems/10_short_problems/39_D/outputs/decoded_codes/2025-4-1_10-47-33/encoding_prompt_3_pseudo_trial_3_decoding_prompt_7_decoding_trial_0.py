def doMain():
    # Step 1: Read input values
    time1 = input()  # Get user input for first time
    time2 = input()  # Get user input for second time

    # Step 2: Split the input strings into components
    timeComponents1 = time1.split()  # Split on whitespace
    timeComponents2 = time2.split()  # Split on whitespace

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare each component of the two time inputs
    for index in range(3):  # Loop through the components (assuming they are always three)
        component1 = int(timeComponents1[index])  # Convert to integer
        component2 = int(timeComponents2[index])  # Convert to integer
        
        # Step 5: Increment the counter if the components are different
        if component1 != component2:  # Compare the components
            differenceCount += 1  # Increment the difference count

    # Step 6: Output the result based on the number of differences
    if differenceCount < 3:  # If less than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Otherwise, output "NO"

# Main execution starts here
if __name__ == "__main__":  # Check if this script is being run as the main program
    doMain()  # Call the main function
