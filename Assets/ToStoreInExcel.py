from openpyxl import Workbook # to convert the data into csv

name,contact,email,items,TotalPrice=0

wb=Workbook()
ws=wb.active
ws.title="Invoice"

ws.append(["Invoice : "])
ws.append(["Name: ",name])
ws.append(["Contact: ",contact])
ws.append(["Email: ",email])
ws.append([])
ws.append(["ProductID","ProductName","QTY","MRP"])
for item in items:
    ws.append(item)

ws.append([])

ws.append(["Total amt: ",TotalPrice])

filename="Invoice1.xlsx"
wb.save(filename)
print(f"invoice saved to {filename}")
