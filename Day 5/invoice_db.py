# 1. libraries
import mysql.connector
from datetime import datetime

# 2. connection established
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="salesdata"    
)
cursor=conn.cursor()
print("check 1: database connection done!")

# 3. query to create table
# 3.1 invoice table : This table is already created using phpmyadmin 
cursor.execute("""
CREATE TABLE IF NOT EXISTS invoice(
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_number VARCHAR(50),
    customer_name VARCHAR(100),
    contact_no VARCHAR(20),
    invoice_date DATE
)
""")
conn.commit()

# 3.2 invoice_items table 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoice_items(
        id INT AUTO_INCREMENT PRIMARY KEY,
        invoice_id INT,
        item_name VARCHAR(100),
        qty INT,
        item_price DECIMAL(10,2),
        amount DECIMAL(10,2)   
    )
''')
conn.commit()

print("check 2: tables are created !")

# 4. Function to create new invoice
def create_invoice(invoice_number,customer_name,contact_no):
    date=datetime.now().date()
    cursor.execute('''
        INSERT INTO invoice (invoice_number,customer_name,contact_no,invoice_date)
        VALUES (%s, %s, %s, %s)
    ''',(invoice_number,customer_name,contact_no,date)
    )
    conn.commit()
    return cursor.lastrowid

# 5. Function to add invoice items
def add_invoice_items(invoice_id,item_name,qty,item_price):
    amount=item_price*qty
    cursor.execute('''
        INSERT INTO invoice_items (invoice_id,item_name,qty,item_price,amount)
        VALUES (%s,%s,%s,%s,%s)
    ''',(invoice_id,item_name,qty,item_price,amount)
    )
    conn.commit()

# 6. Function to display invoice
def display_invoice(invoice_number):
    cursor.execute(
        '''
            SELECT invoice_id,invoice_number,customer_name,contact_no,invoice_date FROM invoice WHERE invoice_number=%s; 
        ''',(invoice_number,)
    )

    invoice=cursor.fetchone()
    if not invoice:
        print("Invalid invoice number")
        return

    invoice_id,invoice_number,customer_name,contact_no,invoice_date=invoice
    print(f'{invoice_id}\n{invoice_number}\n{customer_name}\n{contact_no}\n{invoice_date}')

    cursor.execute('''
        SELECT id,invoice_id,item_name,qty,item_price,amount FROM invoice_items WHERE invoice_id=%s;
    ''',(invoice_id,)
    )

    items=cursor.fetchall()
    if not items:
        print("No sale")
        return 
    
    print("id\ti_id\titem\tqty\tprice\tamount")
    for id,invoice_id,item_name,qty,item_price,amount in items:
        print(f'{id}\t{invoice_id}\t{item_name}\t{qty}\t{item_price}\t{amount}')
    
# 7. User inputs
invoice_number=input("invoice number: ")
customer_name=input("Customer name: ")
contact_no=input("Contact no: ")
invoice_id=create_invoice(invoice_number,customer_name,contact_no)

while(True):
    item_name=input("Item name: ")
    qty=int(input("qty: "))
    price=float(input("Price: "))
    add_invoice_items(invoice_id,item_name,qty,price)

    more=input("Add more items(Y/N): ").lower()
    if more!='y':
        break

display_invoice(input("Enter invoice no: "))

# 8. connection end 
cursor.close()
conn.close()