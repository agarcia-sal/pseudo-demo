# Function to calculate minimum distance and cost for each test case
def calculate_cost(t, test_cases):
    results = []
    for i in range(t):
        m, n, x1, y1, x2, y2, p = test_cases[i]
        
        # Calculate minimum distances on both axes
        x_min = min(abs(x1 - x2), m - abs(x1 - x2))
        y_min = min(abs(y1 - y2), n - abs(y1 - y2))
        
        # Calculate cost
        cost = (x_min + y_min) * p
        
        # Determine result based on cost
        if cost > 1000:
            results.append("Let go of the group.")
        else:
            results.append("You saved the group.")
    
    return results

# Example usage
t = int(input())
test_cases = []
for _ in range(t):
    m, n, x1, y1, x2, y2, p = map(int, input("Enter m, n, x1, y1, x2, y2, p: ").split())
    test_cases.append((m, n, x1, y1, x2, y2, p))

# Get results for each test case
results = calculate_cost(t, test_cases)
for result in results:
    print(result)
