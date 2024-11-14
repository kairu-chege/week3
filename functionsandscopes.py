# function to add two numbers
def add_num(num1, num2):
    sum = num1 + num2
    return sum

Sum = add_num(16, 9)
print(Sum)

# localscope example code

def get_total():
  Total = 10  # Local variable 
  print("Inside the function:", Total)

get_total()
print("Outside the function:", Total)  # This will raise a NameError 
