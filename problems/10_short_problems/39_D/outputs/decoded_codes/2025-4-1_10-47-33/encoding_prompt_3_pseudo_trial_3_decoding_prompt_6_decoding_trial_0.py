def do_main():
    # Step 1: Read input values
    time1 = input()  # Get user input for the first time
    time2 = input()  # Get user input for the second time

    # Step 2: Split the input strings into components
    time_components1 = time1.split()  # Split time1 into components based on whitespace
    time_components2 = time2.split()  # Split time2 into components based on whitespace

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each component of the two time inputs
    for index in range(3):  # Loop through the first three components
        component1 = int(time_components1[index])  # Convert the component from time1 to integer
        component2 = int(time_components2[index])  # Convert the component from time2 to integer
        
        # Step 5: Increment the counter if the components are different
        if component1 != component2:
            difference_count += 1  # If different, increment the count

    # Step 6: Output the result based on the number of differences
    if difference_count < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")   # Print NO if differences are 3 or more

# Main execution starts here
if __name__ == "__main__":
    do_main()  # Call the main function
