def main():
    # Step 1: Read the number of elements from user input
    number_of_elements = int(input())
    
    # Step 2: Initialize boolean list and control variables
    boolean_list = [True] * number_of_elements
    pointer = 0
    index = 1

    # Step 3: Loop to modify the boolean list based on conditions
    while index <= 500000:
        if boolean_list[pointer]:
            boolean_list[pointer] = False
            
        index += 1
        pointer = (pointer + index) % number_of_elements

    # Step 4: Filter for active elements (still True)
    active_elements = [element for element in boolean_list if element]

    # Step 5: Check the result and print the output
    if len(active_elements) == 0:
        print("YES")
    else:
        print("NO")

# Invoke the main function
if __name__ == "__main__":
    main()
