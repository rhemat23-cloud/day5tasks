# Exception Handling Example

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    
    result = numerator / denominator
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

finally:
    print("Program Completed")

