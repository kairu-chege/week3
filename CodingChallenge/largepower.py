def large_power(base, exponent):

  result = base ** exponent
  if result > 5000:
      return True
  else:
      return False

print(large_power(3, 8))  
print(large_power(10, 3))