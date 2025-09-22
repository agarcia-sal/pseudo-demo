def main():
    # Step 1: Take input for two sequences
    sequence1 = input()
    sequence2 = input()

    # Step 2: Split the input sequences into lists of strings
    list1 = sequence1.split()
    list2 = sequence2.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0 

    # Step 4: Compare elements in the two lists
    for index in range(3):  # Assuming we only compare the first 3 elements
        # Convert string elements to integers for comparison
        number_from_list1 = int(list1[index])
        number_from_list2 = int(list2[index])
        
        # Check if the numbers are different
        if number_from_list1 != number_from_list2:
            difference_count += 1 
    
    # Step 5: Determine result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
