import os

def normalize_path():
    # Step 2: Receive Input
    path_input = input().strip()
    
    # Step 3: Normalize Path
    normalized_path = os.path.normpath(path_input)

    # Step 4: Ensure Single Leading Slash
    if normalized_path.startswith('//'):
        normalized_path = '/' + normalized_path.lstrip('/')
    
    # Step 5: Output Result
    print(normalized_path)

# Step 1: Start Program
if __name__ == "__main__":
    normalize_path()
