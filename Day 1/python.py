def calculate_total_distance(left_list, right_list):
    """
    Calculate total distance by repeatedly picking smallest elements from left and right lists.
    
    Args:
    left_list (list): The first list of numbers
    right_list (list): The second list of numbers
    
    Returns:
    int: Total distance between paired smallest elements
    """
    # Create copies of the lists to avoid modifying original lists
    left = left_list.copy()
    right = right_list.copy()
    
    # Sort the lists
    left.sort()
    right.sort()
    
    total_distance = 0
    
    # Continue until one of the lists is empty
    while left and right:
        # Find the smallest element in each list
        left_smallest = min(left)
        right_smallest = min(right)
        
        # Calculate the distance between smallest elements
        distance = abs(left_smallest - right_smallest)
        total_distance += distance
        
        # Remove the smallest elements from their respective lists
        left.remove(left_smallest)
        right.remove(right_smallest)
    
    return total_distance

def read_input_from_file(filename):
    """
    Read input from a file and split into left and right lists.
    
    Args:
    filename (str): Path to the input file
    
    Returns:
    tuple: Two lists of integers (left_list, right_list)
    """
    try:
        with open(filename, 'r') as file:
            left_list = []
            right_list = []
            
            for line in file:
                # Split the line and convert to integers
                left, right = map(int, line.strip().split())
                left_list.append(left)
                right_list.append(right)
            
            return left_list, right_list
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return [], []
    except ValueError:
        print("Error: Invalid input format. Ensure each line contains two integers separated by a space.")
        return [], []

def main():
    # Specify the input file path
    input_filename = 'input.txt'
    
    # Read input from file
    left_list, right_list = read_input_from_file(input_filename)
    
    # Check if lists are not empty
    if left_list and right_list:
        # Calculate and print the total distance
        total_distance = calculate_total_distance(left_list, right_list)
        print(f"Total distance: {total_distance}")
        
        # Optional: Print some additional information
        print(f"Number of input pairs: {len(left_list)}")
        
        # # Print sorted lists for verification
        # print("\nSorted Left List:", sorted(left_list))
        # print("Sorted Right List:", sorted(right_list))

# Executable script
if __name__ == "__main__":
    main()