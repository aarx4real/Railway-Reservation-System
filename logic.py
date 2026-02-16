import random
from tabulate import tabulate
from db_connection import get_connection

def new_user():
    dbo = get_connection()
    co = dbo.cursor()
    pid = random.randint(0, 1000) * 10 # [cite: 12]
    print("\n--- Register Yourself Here ---")
    uid = input("Enter your user id: ") # [cite: 16]
    name = input("Enter your name: ") # [cite: 17]
    pno = input("Enter your phone no: ") # [cite: 18]
    eid = input("Enter your email_id: ") # [cite: 19]
    pwd = input("Enter your password: ") # [cite: 20]
    
    # Corrected SQL execution to prevent errors [cite: 21]
    query = "INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s)"
    co.execute(query, (uid, pid, name, pno, eid, pwd))
    dbo.commit()
    print("**** Congratulations!!! Your id is successfully created ****") # [cite: 22]
    dbo.close()

def admin_add_train():
    dbo = get_connection()
    co = dbo.cursor()
    # Collecting all train details from source inputs [cite: 106-116]
    a = int(input("Enter train no: "))
    b = input("Enter train name: ")
    c = input("Enter train origin: ")
    d = input("Enter train destination: ")
    e = int(input("Enter distance: "))
    g = input("Enter journey time: ")
    h = int(input("Seats AC: "))
    i = int(input("Seats SL: "))
    j = int(input("Seats GEN: "))
    k = int(input("Price AC: "))
    l = int(input("Price SL: "))
    m = int(input("Price GEN: "))
    n = input("Days available: ")
    
    query = "INSERT INTO train_schedule VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    co.execute(query, (a,b,c,d,e,g,h,i,j,k,l,m,n))
    dbo.commit() # [cite: 121]
    print("Train added successfully!")
    dbo.close()

def train_search():
    dbo = get_connection()
    co = dbo.cursor()
    o = input("Enter origin: ") # [cite: 550]
    d = input("Enter destination: ") # [cite: 553]
    co.execute("SELECT * FROM train_schedule WHERE origin LIKE %s AND destination LIKE %s", (f"%{o}%", f"%{d}%"))
    results = co.fetchall()
    if results:
        # Uses tabulate for professional display [cite: 2, 617]
        print(tabulate(results, headers="keys", tablefmt="fancy_grid"))
    else:
        print("No trains found.")
    dbo.close()