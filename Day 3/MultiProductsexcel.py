from datetime import date
from openpyxl import Workbook # to convert the data into csv

# Function to show the Invoice (By selecting option 1)
def show(items,TotalPrice,productCtr,cusDetails):
    print("\n\n\n::::Invoice details::::")
    print(f"{cusDetails[0]}\t\t{date.today()}")
    print(f"{cusDetails[1]}\t\t{cusDetails[2]}")
    print("-*---------------------------*-")
    print("Id\t\tName\t\tqty\tMRP")
    for i in range(0,productCtr):
        print(f"{items[i][0]}\t\t{items[i][1]}\t\t{items[i][2]}\t{items[i][3]}")
        print("-----------------------------")
    print("Total Price  :   ",TotalPrice)

# Function to add the product in Invoice (By selecting option 0)
def addProduct(items,TotalPrice,productCtr):
    productId=(input("Enter productId: "))
    productName=(input("Enter product Name: "))
    qty=input("Enter qty of product: ")
    while(True):
        if qty.isdigit()==False:
            qty=input("Enter qty of product: ")
        else:
            qty=(int(qty))
            break        
    priceOfProduct=input("Enter MRP:")
    while(True):
        if priceOfProduct.isdigit()==False:
            priceOfProduct=input("Enter valid MRP:")
        else:
            priceOfProduct=(int(priceOfProduct))
            break
    items.append([productId,productName,qty,priceOfProduct])
    TotalPrice+=int(priceOfProduct)*int(qty)
    productCtr+=1
    return items,TotalPrice,productCtr

# Function to delete the product from Invoice (By selecting option 2)
def delete(items,productCtr,TotalPrice,productId):
    productCtr-=1
    for i in items:
        if i[0]==productId:
            TotalPrice-=(i[2]*i[3])
            items.remove(i)
    return items,productCtr,TotalPrice

# Customer details:-
cusDetails=[] 
# 1. name 2. phoneNumber 3. email

cusDetails.append(input("Enter customer name: "))

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
        cusDetails.append(phone_number)
        break
cusDetails.append(input("Enter email ID: "))

# Items list:-
items=[] # Items and its details
TotalPrice=0 # Final price to be paid : initially 0
productCtr=0 #Product count : initially 0
while(True):
    choice=input("choose\n0: to add product\n1: to show invoice\n2: to remove product\n")
    if choice in ['0','1','2']:
        choice=int(choice)
        if choice==0:
            items,TotalPrice,productCtr=addProduct(items,TotalPrice,productCtr)
        elif choice==1:
            show(items,TotalPrice,productCtr,cusDetails)
        else:
           items,productCtr,TotalPrice=delete(items,productCtr,TotalPrice,input("Enter product Id: ")) 
    else:
        print("!!!Invalid choice!!!")
        break

wb=Workbook()
ws=wb.active
ws.title="Invoice"

ws.append(["Invoice : "])
ws.append(["Name: ",cusDetails[0]])
ws.append(["Contact: ",cusDetails[1]])
ws.append(["Email: ",cusDetails[2]])
ws.append([])
ws.append(["ProductID","ProductName","QTY","MRP"])
for item in items:
    ws.append(item)

ws.append([])

ws.append(["Total amt: ",TotalPrice])

filename="Invoice1.xlsx"
wb.save(filename) 
print(f"invoice saved to {filename}")
