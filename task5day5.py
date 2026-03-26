# Generator function for squares
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

# Normal list of squares
def square_list(n):
    return [i * i for i in range(1, n + 1)]

# Example usage
n = 5

# Using list
list_squares = square_list(n)
print("List:", list_squares)
print("Type of list_squares:", type(list_squares))

# Using generator
gen_squares = square_generator(n)
print("Generator object:", gen_squares)
print("Type of gen_squares:", type(gen_squares))

# Consuming generator
print("Squares from generator:", list(gen_squares))
