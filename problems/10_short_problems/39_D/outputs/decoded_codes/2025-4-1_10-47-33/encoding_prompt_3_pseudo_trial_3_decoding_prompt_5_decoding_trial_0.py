def do_main():
    # Step 1: Read input values
    time1 = input()  # get user input for first time
    time2 = input()  # get user input for second time

    # Step 2: Split the input strings into components
    time_components1 = time1.split()  # split time1 into components based on whitespace
    time_components2 = time2.split()  # split time2 into components based on whitespace

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each component of the two time inputs
    for index in range(3):  # loop from 0 to 2
        component1 = int(time_components1[index])  # convert timeComponents1[index] to integer
        component2 = int(time_components2[index])  # convert timeComponents2[index] to integer
        
        # Step 5: Increment the counter if the components are different
        if component1 != component2:  # if components are not equal
            difference_count += 1  # increment differenceCount

    # Step 6: Output the result based on the number of differences
    if difference_count < 3:  # if differences are less than 3
        print("YES")  # output "YES"
    else:
        print("NO")  # otherwise, output "NO"

# Main execution starts here
if __name__ == "__main__":
    do_main()  # call the main function
