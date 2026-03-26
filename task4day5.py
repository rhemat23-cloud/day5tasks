def factorial(n):
    # Handle negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Base case: 0! = 1
    if n == 0:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Example usage
try:
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError as e:
    print("Error:", e)
