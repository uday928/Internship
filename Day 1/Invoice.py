# 

name=input("Enter customer name: ")
phone_number=input("Enter your contact number: ")
while(True):
    if phone_number.isdigit()==False:
        print("Phone number should not have non-numeric characters!!!")
        phone_number=input("Enter valid contact number: ")        
    elif int(str(phone_number)[0])<6:
        print("Phone number should start with 6,7,8,9!!!")
        phone_number=input("Enter Valid contact number: ")
    elif  len(str(phone_number))!=10:
        print("Phone number should be 10 digits long!!!")
        phone_number=input("Enter valid contact number: ")
    else:
        break
# print(phone_number)
email=input("Enter email ID: ")
productId=input("Enter productId: ")
productName=input("Enter product Name: ")
qty=input("Enter qty of product: ")
while(True):
    if qty.isdigit()==False:
        qty=input("Enter qty of product: ")
    else:
        qty=int(qty)
        break        
priceOfProduct=input("Enter MRP:")
while(True):
    if priceOfProduct.isdigit()==False:
        priceOfProduct=input("Enter valid MRP:")
    else:
        priceOfProduct=int(priceOfProduct)
        break
TotalPrice=priceOfProduct*qty

print("\n\n\n::::Invoice details::::")
print(name,"          ","20-01-2026")
print(phone_number,"    ",email)
print("productId    :   ",productId)
print("ProductName  :   ",productName)
print("qty          :   ",qty)
print("MRP          :   ",priceOfProduct)
print("Total Price  :   ",TotalPrice)