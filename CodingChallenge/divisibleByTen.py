def divisible_by_ten(num): # define the function to accept one argument num
    mod = num % 10      # calculate the reminder of the input divided by 10 using modulus
    if mod == 0:
        return True
    else:
        return False
    
print(divisible_by_ten(10))
print(divisible_by_ten(12))