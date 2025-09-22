def calculate_min_cost(T):
    for t in range(T):
        # Read N, K and list A
        (N,K) = map(int,str(input()).split())
        A = list(map(int,str(input()).split()))
        
        min_cost = 1000000  # Initialize min_cost to a large number

        # Iterate over the range from min(A) to max(A) + 1
        for i in range(min(A), max(A) + 1):
            # Compute and sort costs for A
            costs = []
            for num in A:
                if i < num:
                    cost = 5 * (num - i)
                else:
                    cost = 3 * (i - num)
                costs.append(cost)
            
            # Sort the costs and take the sum of the first K costs
            costs.sort()
            current_cost = sum(costs[:K])
            
            # Update min_cost if current_cost is less
            if current_cost < min_cost:
                min_cost = current_cost
        
        # Print the minimum cost for the current test case
        print(min_cost)

# Example usage:
T = int(input())  # Number of test cases

calculate_min_cost(T)
