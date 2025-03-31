#Define the function
def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount_amount=price*(discount_percent/100)
        final_price=price-discount_amount
        return final_price
    else:
        return price

#Get input from user
price=float(input("Enter the original price:"))
discount_percent=float(input("Enter the discount percentage:"))

#Calculate final price
final_price=calculate_discount(price, discount_percent)

print("The final price is:",final_price)
