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
    # To find the duplicate value
    cursor.execute('''
        SELECT * FROM invoice WHERE invoice_number=%s;
    ''',(invoice_number,))
    res=cursor.fetchone()
    if res!=None:
        print("Duplicate found")
        return None
    # ------------------------------------------------------
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
    
# 7. Function to delete invoice from table
def delete(invoice_number):
    cursor.execute('''
        SELECT invoice_id FROM invoice WHERE invoice_number=%s; 
    ''',(invoice_number,))
    res=cursor.fetchone()
    if not res:
        print("Invoice not found!")
        return
    inv_id=res[0]
    cursor.execute('''
        DELETE FROM invoice_items WHERE invoice_id=%s;
    ''',(inv_id,))
    conn.commit()
    print("Records have been deleted from invoice items!!!")

    cursor.execute('''
        DELETE FROM invoice WHERE invoice_number=%s;
    ''',(invoice_number,))
    conn.commit()
    print("Record has been deleted from invoice table!!!")

# 8. Function to update in table:
def update_cus_details(invoice_number):
    ch=['1','2']
    choice=input("1: To update name\n2: To update contact number\nEnter:")
    if choice in ch:
        if choice=='1':
            ip=input("Customer name: ")
            cursor.execute('''
                UPDATE invoice SET customer_name=%s WHERE invoice_number=%s; 
            ''',(ip,invoice_number,)) 
            conn.commit()
            print("Name is updated!!!")
        else:
            ip=input("Contact no: ")
            while (not ip.isdigit()) or len(ip) != 10 or int(ip[0]) < 6:
                ip = input("Enter valid 10-digit phone number starting with 6-9: ")
            cursor.execute('''
                UPDATE invoice SET contact_no=%s WHERE invoice_number=%s; 
            ''',(ip,invoice_number,))
            conn.commit()
            print("contact is updated!!!")
    else:
        print("Invalid choice")
        return

# 9. User inputs
chList=['1','2','3','4']
# invoice_number,invoice_id,customer_name,contact_no,item,qty,price
while True:
    choice=input('''
        1: create new invoice
        2: Generate bill
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
        while(True and invoice_id!=None):
            item_name=input("Item name: ")
            qty=int(input("qty: "))
            price=float(input("Price: "))
            add_invoice_items(invoice_id,item_name,qty,price)

            more=input("Add more items(Y/N): ").lower()
            if more!='y':
                break
    elif choice=='2':
        print("Coming soon...")
    elif choice=='3':
        delete(input("Enter invoice number: "))
    elif choice=='4':
        display_invoice(input("Enter invoice no: "))
    elif choice=='5':
        update_cus_details(input("Enter invoice number: "))
    else:
        print("End of the session!!!")
        break    
# 10. connection end 
cursor.close()
conn.close()