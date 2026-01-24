# Invoice

# 1. Customer details
name=input("Enter customer name: ")
phone_number=input("Enter your contact number: ")
# 1.1 Phone number verification
while(True):
    # Number should be of in digit format
    if phone_number.isdigit()==False:
        print("Phone number should not have non-numeric characters!!!")
        phone_number=input("Enter valid contact number: ")
    # Number should not start with 1 to 5 to prevent 1234567890 like fake numbers 
    elif int(str(phone_number)[0])<6:
        print("Phone number should start with 6,7,8,9!!!")
        phone_number=input("Enter Valid contact number: ")
    # Number length should be 10 digits long
    elif  len(str(phone_number))!=10:
        print("Phone number should be 10 digits long!!!")
        phone_number=input("Enter valid contact number: ")
    else:
        break
# print(phone_number) #check
email=input("Enter email ID: ")

# 2. Product details
productId=input("Enter productId: ")
productName=input("Enter product Name: ")
qty=input("Enter qty of product: ")
# 2.1 qty input chec
while(True):
    # qty IP should  be in digit
    if qty.isdigit()==False:
        qty=input("Enter qty of product: ")
    else:
        qty=int(qty)
        break        
priceOfProduct=input("Enter MRP:")
# 2.2 Price input check
while(True):
    # price should be in digit format
    if priceOfProduct.isdigit()==False:
        priceOfProduct=input("Enter valid MRP:")
    else:
        priceOfProduct=int(priceOfProduct)
        break
TotalPrice=priceOfProduct*qty

# 3. Output
print("\n\n\n::::Invoice details::::")
print(name,"          ","20-01-2026")
print(phone_number,"    ",email)
print("productId    :   ",productId)
print("ProductName  :   ",productName)
print("qty          :   ",qty)
print("MRP          :   ",priceOfProduct)
print("Total Price  :   ",TotalPrice)