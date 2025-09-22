def main():
    # Step 2: Input
    n = int(input())

    # Step 3: Initialize
    is_active = [True] * n
    current_index = 0
    increment = 1

    # Step 4: Loop through increments up to 500,000
    for _ in range(500000):
        if is_active[current_index]:
            is_active[current_index] = False
        
        increment += 1
        current_index = (current_index + increment) % n

    # Step 5: Check for Active Elements
    active_elements = [index for index, state in enumerate(is_active) if state]

    # Step 6: Output the results
    if len(active_elements) == 0:
        print('YES')
    else:
        print('NO')

# Step 1: Begin Process
if __name__ == "__main__":
    main()
