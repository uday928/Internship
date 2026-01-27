# 1. libraries
import mysql.connector
from datetime import datetime

# 2. connection established
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="salesdata",
    port=3305
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
    print(f'invoice_id: {invoice_id}\ninvoice_number: {invoice_number}\nname: {customer_name}\ncontact: {contact_no}\ndate: {invoice_date}')

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

    cursor.execute('''
        SELECT SUM(amount) FROM invoice_items WHERE invoice_id=%s;
    ''',(invoice_id,))

    t_amt=cursor.fetchone()[0]
    print(f'Total price: {t_amt}')
    
# 7. User inputs

chList=['1','2','3','4']
# invoice_number,invoice_id,customer_name,contact_no,item,qty,price
while True:
    choice=input('''
        1: create new invoice
        3: delete 
        4: show
        5: update
    ''')
    if choice=='1':
        invoice_number=input("invoice number: ")
        customer_name=input("Customer name: ")
        contact_no=input("Contact no: ")
        while (not contact_no.isdigit()) or len(contact_no) != 10 or int(contact_no[0]) < 6:
            contact_no = input("Enter valid 10-digit phone number starting with 6-9: ")
        invoice_id=create_invoice(invoice_number,customer_name,contact_no)
        print("welcome!!!",customer_name)
        while(True):
            item_name=input("Item name: ")
            qty=int(input("qty: "))
            price=float(input("Price: "))
            add_invoice_items(invoice_id,item_name,qty,price)

            more=input("Add more items(Y/N): ").lower()
            if more!='y':
                break
    elif choice=='3':
        # To be updated
        print("Coming soon...")
    elif choice=='4':
        display_invoice(input("Enter invoice no: "))
    elif choice=='5':
        # To be updated
        print("Coming soon...")
    else:
        print("End of the session!!!")
        break    
# 8. connection end 
cursor.close()
conn.close()