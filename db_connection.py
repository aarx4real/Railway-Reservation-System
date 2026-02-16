import mysql.connector as con

def get_connection():
    return con.connect(
        host="localhost",
        user="root",
        password="admin",
        database="train_reservation"
    )