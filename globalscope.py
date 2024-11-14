global_var = 10

def add_nums(num1, num2):
  """Adds two numbers and the global variable."""
  result = num1 + num2 + global_var
  return result

def double_it(num):
  """Doubles a number and adds the global variable."""
  result = num * 2 + global_var
  return result

# Example usage:
sum_result = add_nums(5, 3)
double_result = double_it(4)

print("Sum:", sum_result)  # Output: 18
print("Doubled:", double_result)  # Output: 18