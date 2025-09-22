# Step 1: Input
number = abs(int(input()))

# Step 2: Initialize
index = 0

# Step 3: Loop indefinitely
while True:
    # Step 3a: Calculate Triangular Number
    triangularSum = (index * (index + 1)) // 2
    
    # Step 3b: Calculate Difference
    difference = triangularSum - number
    
    # Step 3c: Check Conditions
    if triangularSum == number:
        print(index)
        break
    elif triangularSum > number:
        if difference % 2 == 0:
            print(index)
            break
    
    # Step 3d: Increment Counter
    index += 1


def find_triangular_number():
    number = abs(int(input()))
    index = 0

    while True:
        triangularSum = (index * (index + 1)) // 2
        difference = triangularSum - number

        if triangularSum == number:
            return index
        elif triangularSum > number:
            if difference % 2 == 0:
                return index

        index += 1

result = find_triangular_number()
if result is not None:
    print(result)
