def is_safe_report(report):
    """
    Determines if a report is safe based on the given rules.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    # Check if differences are all positive (increasing) or all negative (decreasing)
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)
    
    # Check if all differences are between 1 and 3 inclusive
    are_differences_valid = all(1 <= abs(diff) <= 3 for diff in differences)
    
    # The report is safe if it is entirely increasing or decreasing and has valid differences
    return (is_increasing or is_decreasing) and are_differences_valid

def is_safe_with_dampener(report):
    """
    Determines if a report is safe with the Problem Dampener applied.
    """
    if is_safe_report(report):
        return True

    # Check if removing one level makes the report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove the i-th level
        if is_safe_report(modified_report):
            return True

    return False

def count_safe_reports_with_dampener(file_path):
    """
    Counts the number of safe reports, accounting for the Problem Dampener.
    """
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                levels = list(map(int, line.strip().split()))
                if is_safe_with_dampener(levels):
                    safe_count += 1
    return safe_count

# Read input from input.txt and count safe reports with the Problem Dampener
file_path = "input.txt"
safe_reports = count_safe_reports_with_dampener(file_path)
print(f"Number of safe reports with the Problem Dampener: {safe_reports}")
