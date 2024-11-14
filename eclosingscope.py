# Enclosing scope is a scope of a function that is defined within another function
# we can access variables from the enclosing scope within the inner function using the nonlocal keyword.

def outer_function():
  x = 15
  
  def inner_function():
    nonlocal x
    x += 5
    print("Inside inner function:", x)
    
  inner_function()
  print("Inside outer function:", x)
  
outer_function()