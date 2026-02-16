from logic import new_user, add_train, book_ticket, cancel_ticket

def passenger_panel(uid):
    while True:
        print("\n--- PASSENGER PANEL ---")
        print("1. Book Ticket\n2. Cancel Ticket\n3. Logout")
        ch = input("Choice: ")
        if ch == '1': book_ticket(uid)
        elif ch == '2': cancel_ticket()
        elif ch == '3': break

def main_menu():
    while True:
        print("\n--- RAILWAY SYSTEM ---")
        print("1. Admin\n2. Login/Register\n3. Exit")
        ch = input("Choice: ")
        if ch == '1':
            if input("Admin Pwd: ") == "CLASS12CS": 
                # call admin functions
                pass 
        elif ch == '2':
            # In a real app, you'd check login here
            uid = input("Enter User ID to login: ")
            passenger_panel(uid)
        elif ch == '3': break

if __name__ == "__main__":
    main_menu()