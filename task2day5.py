def calculate_total(*numbers):
    """
    Calculates the sum of all numbers provided as arguments.
    Args:
        *numbers: Variable length argument list of numbers (int or float)
    Returns:
        float: Sum of all numbers
    """
    # Check if all inputs are numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All inputs must be numbers")

    # Return the total sum
    return sum(numbers)

# Example usage
if __name__ == "__main__":
    try:
        total1 = calculate_total(10, 20, 30)
        print("Total of 10, 20, 30 is:", total1)

        total2 = calculate_total(5, 12.5, 7, 0.5)
        print("Total of 5, 12.5, 7, 0.5 is:", total2)

        # An example with no input, should return 0
        total3 = calculate_total()
        print("Total with no inputs is:", total3)

        # If a non-numeric value is passed, it raises an error
        # total4 = calculate_total(10, 'a')  # Uncommenting this will raise ValueError
    except ValueError as e:
        print("Error:", e)
