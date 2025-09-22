def main():
    # Step 1: Input two strings
    string1 = input()
    string2 = input()

    # Step 2: Split the strings into lists of substrings
    list1 = string1.split()
    list2 = string2.split()

    # Step 3: Initialize counter for differences
    differences_count = 0 

    # Step 4: Compare the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        number1 = int(list1[index])
        number2 = int(list2[index])
        
        # Step 5: Check for differences
        if number1 != number2:
            differences_count += 1
            
    # Step 6: Determine the final result 
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Main execution block
if __name__ == "__main__":
    main()
