def calculate_discount(price, discount_percent):
    
    if discount_percent >= 0.2:
        discount_amount = price * discount_percent
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# getting input from the user
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage (e.g., 20 for 20%):")) / 100

# calculating the final price 
final_price = calculate_discount(price, discount_percent)

print("Final price:", final_price)