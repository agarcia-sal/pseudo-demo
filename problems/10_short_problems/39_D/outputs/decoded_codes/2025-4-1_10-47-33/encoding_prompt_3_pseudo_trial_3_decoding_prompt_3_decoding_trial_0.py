def do_main():
    # Step 1: Read input values
    time1 = input()
    time2 = input()

    # Step 2: Split the input strings into components
    time_components1 = time1.split()
    time_components2 = time2.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each component of the two time inputs
    for index in range(3):
        # Convert string components to integers
        component1 = int(time_components1[index])
        component2 = int(time_components2[index])
        
        # Step 5: Increment the counter if the components are different
        if component1 != component2:
            difference_count += 1

    # Step 6: Output the result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    do_main()
